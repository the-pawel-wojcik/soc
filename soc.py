#!/usr/bin/env python3

"""
Created on Jan 29th 2024 by Paweł Wójcik.
The purpose of this script is to find the impact of SOCs on the spectrum of a
molecule.
"""

import argparse
import sys
import numpy as np

import printing as pr
import plt_soc

eV2cm = 8065.479
cm2eV = 1.0/eV2cm

CARTESIAN = ["x", "y", "z"]


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('data')
    parser.add_argument('-b', '--subblock', default=None,
                        type=str, help="columns,rows use XAB")
    parser.add_argument('-e', '--eigenvectors', default="", type=str,
                        help="Print eigenvectors, 'a' for ascii 'l' for latex."
                        )
    parser.add_argument('-H', '--Hamiltonian', default=False,
                        action='store_true',
                        help="Print the Hamiltonian matrix.")
    parser.add_argument('-l', '--show_largest',
                        default=False, action='store_true')
    parser.add_argument('-p', '--plot', default="", type=str,
                        help='Plot t for TDMs.')
    parser.add_argument('-r', '--branching_ratios', default=None, type=int,
                        help="Show decay branching ratios from the state <#>")
    parser.add_argument('-t', '--threshold', default=0.1,
                        type=float, help="Print threshold")
    args = parser.parse_args()
    return args


def introduce_order(states: list[dict]) -> int:
    """
    Adds to every state the key 'position' under which is a list of two
    integers. Those integers mark the subblock of the Hamiltonian (the first
    element and one after the last) that corresponds to this state.

    Return:
        dim: int the dimension of the Hamiltonian
    """
    dim = 0
    for state in states:
        multiplicity = state['multiplicity']
        state['position'] = [dim, dim + multiplicity]
        dim += multiplicity
    return dim


def find_positions(new: dict, knowns: list[dict]) -> list[int] | None:
    new_irrep = new['irrep']
    new_mlp = new['multiplicity']
    for known in knowns:
        if known['irrep'] != new_irrep:
            continue
        if known['multiplicity'] != new_mlp:
            continue
        return known['position']
    return None


def add_order_to_SOC(states: list[dict], socs: list[dict]):
    """
    Edits the `socs` elements by adding to their `bra` and `ket` dictionaries
    the `position` key. The value stored under `position` is the range of
    indices that the states are assigned to in the state interaction
    Hamiltonian.
    """
    for soc in socs:
        bra = soc['bra']
        bra_pos = find_positions(bra, states)
        if bra_pos is None:
            print(f"Error! SOC computed for an unknown state: {bra}",
                  file=sys.stderr)
            continue
        bra['position'] = bra_pos

        ket = soc['ket']
        ket_pos = find_positions(ket, states)
        if ket_pos is None:
            print(f"Error! SOC computed for an unknown state: {ket}",
                  file=sys.stderr)
            continue
        ket['position'] = ket_pos


def construct_Hamiltonian_matrix(
        dim: int,
        states: list[dict],
        socs_aggregate: list[dict],
) -> np.ndarray:
    """
    Constructs a matrix of the spin-orbit couplings.
    All energies in wavenumber.

    Returns:
        None.

    """

    soc_matrix = np.zeros((dim, dim), dtype=np.cdouble)

    """
    Add state energies on the diagonal
    """
    for state in states:
        pos = state['position']
        energy_eV = state['energy']['E ex']['eV']
        energy_cm = energy_eV * eV2cm
        diagonal_energy = np.eye(state['multiplicity'], dtype=np.cdouble)
        diagonal_energy *= energy_cm
        # diagonal_energy *= energy_eV
        soc_matrix[pos[0]:pos[1], pos[0]:pos[1]] = diagonal_energy

    """
    Add matrix elements of the SOC part of the Breit-Pauli Hamiltonian
    """
    for soc in socs_aggregate:
        bra_pos = soc['bra']['position']
        ket_pos = soc['ket']['position']
        mel = np.array(soc['H SO'], dtype=np.cdouble)
        soc_matrix[bra_pos[0]:bra_pos[1], ket_pos[0]:ket_pos[1]] = mel
        mel_hc = np.conjugate(mel.T)
        soc_matrix[ket_pos[0]:ket_pos[1], bra_pos[0]:bra_pos[1]] = mel_hc

    return soc_matrix


def construct_tdms_matrix_vec(
        dim: int,
        states: list[dict],
        trans_props_aggregate: list[dict]
) -> dict[str, np.ndarray]:
    """
    Constructs a matrix of the dipole moment operator. The dipole moment is a
    vector and so the matrix is a vector. The three components of the vector
    are stored as matrices under the 'x', 'y', and 'z' keys of the output dict.

    The state-diagonal part of each matrix are the state dipole moments. The
    state-off-diagonal part of each matrix are the transition dipole moments.
    """

    # dipole moment matrices
    dmms = {key: np.zeros((dim, dim)) for key in CARTESIAN}

    """
    TODO: Add state's dipole moments.
    """

    """
    Add transition dipole moments
    """
    for trans_prop in trans_props_aggregate:
        bra_pos = trans_prop['bra']['position']
        ket_pos = trans_prop['ket']['position']
        dim_bra = trans_prop['bra']['multiplicity']
        dim_ket = trans_prop['ket']['multiplicity']
        tdm_vec = trans_prop['tdm']

        for cart in CARTESIAN:
            tdm = tdm_vec[cart]
            # build a submatrix of tdms
            # It contains the same TDM value as its entry
            # TODO: is this really `np.ones`? Figure out what exactly are the
            # selection rules for changes in the spin projection.
            # HINT: tdm would be non-zero only when dim_bra == dim_ket because
            # spin-changing transitions are forbidden in the electronic
            # Hamiltonian
            mel = tdm * np.ones(shape=(dim_bra, dim_ket))
            if dim_bra != dim_ket and tdm != 0.0:
                print(
                    f"Info: non-zero {tdm=:.3f} in a spin-chaning transition",
                    file=sys.stderr,
                )

            dmms[cart][bra_pos[0]:bra_pos[1], ket_pos[0]:ket_pos[1]] = mel
            # for some reason TDMs are real
            dmms[cart][ket_pos[0]:ket_pos[1], bra_pos[0]:bra_pos[1]] = mel.T

    return dmms


def soc_max_helper(soc):
    matrix = soc['H SO']
    row_maxes = [max(row, key=lambda z: abs(z)) for row in matrix]
    matrix_max_value = max(row_maxes, key=lambda z: abs(z))
    return abs(matrix_max_value)


def find_largest_soc(socs):
    socs.sort(key=soc_max_helper, reverse=True)
    how_many = 10
    print("The largest SOC elements:")
    for i, soc in enumerate(socs[0:how_many]):
        print(f"Position {i}")
        print(f"ket: {soc['ket']['irrep']} {soc['ket']['multiplicity']}")
        print(f"bra: {soc['bra']['irrep']} {soc['bra']['multiplicity']}")
        for row in soc['H SO']:
            for val in row:
                print(f"({val.real:+.2f},{val.imag:+.2f})", end='')
            print('')


def prepare_subblock_ranges(args, dim):
    """
    Warning: This is a quinone-specific option
    """
    rows = [i for i in range(dim)]
    cols = [i for i in range(dim)]

    if args.subblock is None:
        return rows, cols

    subblocks = args.subblock
    if ',' not in subblocks:
        print("Error, incorrect subblocks. Try X,X or X,AB.",
              file=sys.stderr)
        return
    rows_str, cols_str = args.subblock.split(',')
    ranges = {
        'X': [i for i in range(4)],
        'A': [i for i in range(4, 12)],
        'B': [i for i in range(12, 20)],
    }

    rows = []
    for lttr in rows_str:
        rows += ranges[lttr]
    rows.sort()

    cols = []
    for lttr in cols_str:
        cols += ranges[lttr]
    cols.sort()
    return rows, cols


def main():
    args = get_args()
    # The data file is a python script that contains
    # only definitions of variables: states, ref2eom and eom2eom
    data = {}
    with open(args.data) as data_file:
        exec(data_file.read(), globals(), data)

    states = data['states']
    # This function changes the states dictionary by adding the 'position' key
    # to every states
    dim = introduce_order(states)

    # In the model EOM that I have used, the CCSD reference state was one of
    # the target states. Such model produces two sets of transition properties:
    # REF <--> EOM and EOM <--> EOM Despite the need for a separate
    # calculations, both sets of data correspond to transitions between
    # equivalent states of interest.
    trans_props = data['eom2eom']
    if 'ref2eom' in data:
        trans_props_ref2eom = data['ref2eom']
        trans_props += trans_props_ref2eom

    add_order_to_SOC(states, trans_props)

    hamiltonian = construct_Hamiltonian_matrix(dim, states, trans_props)
    evalues, evectors = np.linalg.eigh(hamiltonian)

    tdms_vec = construct_tdms_matrix_vec(dim, states, trans_props)

    # Find SOC-corrected transition dipole moments
    soc_tdms_vec = {}
    for cart in CARTESIAN:
        soc_tdms_vec[cart] = \
            evectors.conjugate().transpose() @ tdms_vec[cart] @ evectors

    soc_tdms_abs2 = np.zeros(shape=(dim, dim), dtype=np.float32)
    for cart in CARTESIAN:
        soc_tdms_abs2 += np.power(np.abs(soc_tdms_vec[cart]), 2)

    # Output generation
    rows, cols = prepare_subblock_ranges(args, dim)

    if args.Hamiltonian is True:
        pr.print_submatrix(hamiltonian, rows, cols,
                           title="SOCs + diagonal energies")

    if 'H' in args.plot:
        plt_soc.show_Hamiltonian(
            hamiltonian,
            title="the SOC Hamiltonian"
        )
        vHv = evectors.conjugate().transpose() @ hamiltonian @ evectors
        plt_soc.show_Hamiltonian(
            vHv,
            title="the SOC Hamiltonian\nafter diagonalization."
        )

    pr.deal_with_spectrum_printing(args, cols, evalues, evectors, states)

    if 't' in args.plot:
        for cart in CARTESIAN:
            plt_soc.show_real_matrix(tdms_vec[cart], f"TDM {cart}")

        for cart in CARTESIAN:
            plt_soc.show_real_matrix(soc_tdms_vec[cart].real,
                                     f"SOC-TDM {cart} real")
            plt_soc.show_real_matrix(soc_tdms_vec[cart].imag,
                                     f"SOC-TDM {cart} imag")

        plt_soc.show_real_matrix(soc_tdms_abs2, "|SOC-TDM|$^2$")

    pr.print_branching_ratios(args, dim, evalues, soc_tdms_abs2)

    if args.show_largest is True:
        find_largest_soc(trans_props)


if __name__ == "__main__":
    main()
