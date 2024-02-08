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

eV2cm = 8065.479
cm2eV = 1.0/eV2cm


def get_args():
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
    parser.add_argument('-t', '--threshold', default=0.1,
                        type=float, help="Print threshold")
    args = parser.parse_args()
    return args


def introduce_order(states):
    """
    Adds to every state the attribute 'position' which is a list of two
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


def find_positions(new, knowns):
    new_irrep = new['irrep']
    new_mlp = new['multiplicity']
    for known in knowns:
        if known['irrep'] != new_irrep:
            continue
        if known['multiplicity'] != new_mlp:
            continue
        return known['position']
    return None


def add_order_to_SOC(states, socs):
    """
    Edits the `socs` elements by adding to their `bra` and `ket` dictionaries
    the `position` key. The `position` value is the range of indices that the
    states are assigned to in the state interaction Hamiltonian.
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


def construct_Hamiltonian_matrix(dim, states, socs_aggregate):
    """
    Constructs a matrix of the spin-orbit couplings.
    All energies in wavenumber.

    Returns:
        None.

    """

    # carte blanche
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
        print(soc['H SO'])


def prepare_subblock_ranges(args, dim):
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

    # In the model EOM that I have used the CCSD reference state was one of the
    # target states. There are thus two sets of transition properties:
    # REF <--> EOM and EOM <--> EOM
    # Despite the need for a separate calculations, both sets of data
    # correspond to transitions between states of interests.
    socs_ref2eom = data['ref2eom']
    socs_eom2eom = data['eom2eom']
    socs_aggregate = socs_ref2eom + socs_eom2eom

    add_order_to_SOC(states, socs_aggregate)

    hamiltonian = construct_Hamiltonian_matrix(dim, states, socs_aggregate)

    rows, cols = prepare_subblock_ranges(args, dim)

    if args.Hamiltonian is True:
        pr.print_submatrix(hamiltonian, rows, cols,
                           title="SOCs + diagonal energies")

    evalues, evectors = np.linalg.eigh(hamiltonian)

    pr.deal_with_spectrum_printing(args, cols, evalues, evectors, states)

    if args.show_largest is True:
        find_largest_soc(socs_aggregate)


if __name__ == "__main__":
    main()
