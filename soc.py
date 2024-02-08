#!/usr/bin/env python3

"""
Created on Jan 29th 2024 by Paweł Wójcik.
The purpose of this script is to find the impact of SOCs on the spectrum of a
molecule.
"""

import argparse
import sys
import numpy as np
import cmath as m

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
    parser.add_argument('-l', '--show_largest',
                        default=False, action='store_true')
    parser.add_argument('-t', '--threshold', default=0.1,
                        type=float, help="Print threshold")
    args = parser.parse_args()
    return args


def state2latex(state):
    irrep = state['irrep']
    irrepN, irrep_lbl = irrep.split('/')

    irrep_lttr = irrep_lbl[0]
    irrep_decorator = ""
    irrep_extra = irrep_lbl[1:]
    if irrep_extra == "":
        irrep_decorator = ""
    elif irrep_extra == "'":
        irrep_decorator = r' ^{\prime}'
    elif irrep_extra == '"':
        irrep_decorator = r' ^{\prime\prime}'
    else:
        irrep_decorator = r' _{' + irrep_extra + '}'

    multiplicity = state['multiplicity']
    spin_z = state['spin_z']
    out = r'\ket{' + irrepN + ' ^{' + str(multiplicity) + '} '
    out += irrep_lttr + irrep_decorator + ', ' + f"{spin_z:2d}" + '}'
    return out


def print_vector_latex(v,
                       already_sorted: bool = False,
                       polar: bool = False,
                       norm_threshold: float = 0.1,
                       latex_eom_states: bool = False):
    r"""
    Prints an eigenvector of the soc-hamiltonian by listing the basis
    vectors that have an amplitude (modulus square of its coefficient)
    larger than 0.01.
    Output is formatted in a latex format

    Parameters
    ----------
    v : eigenvector
        v = c_{i_0} |i_0> + \ldots
        In each pair the [0] element is i_0, and the [1] element is c_{i_0}
    polar (bool, optional): $1 ^2 \Sigma$  vs '1'. Defaults to False.
    norm_threshold (float, optional):
        print "c_{i_0} |i_0>" if |c_{i_0}| > norm_threshold
    latex_eom_states (bool, optional): $1 ^2 \Sigma$  vs '1'.
        Defaults to False.


    Returns
    -------
    output : string
        Latex-formatted presentation of v

    """
    vector = [[i, val] for i, val in enumerate(v)]
    vector.sort(key=lambda z: abs(z[1]), reverse=True)
    small_contributions = False
    output = ""
    output += "$"
    for coeff in vector:
        norm = abs(coeff[1])
        if norm > norm_threshold:
            if polar:
                phi = m.phase(coeff[1]) / m.pi
                output += f"{norm:4.3f}"
                if abs(phi) > 0.01:
                    output += r"e^{" + f"{phi:+3.2f}" + r"\pi i} "
            else:
                output += f"{coeff[1].real:+3.2f}"
                output += f"{coeff[1].imag:+3.2f}i"
            # HINT: `label` is the right place to go fancy
            label = coeff[0]
            output += r"\ket{"
            if latex_eom_states:
                output += f"{label}"
            else:
                output += f"{coeff[0]:2d}"
            output += "}"
            output += " "
            if polar:
                output += "+ "
        elif norm > 1e-16:
            small_contributions = True
    if small_contributions:
        if polar:
            output += r"\ldots"
        else:
            output += r"+ \ldots"
    output += "$"
    return output


def print_submatrix(h, rows, cols, title: str = ""):

    rows.sort()

    print(f"Printing: {title}")
    print('   ', end='')

    if len(h) < rows[-1] + 1:
        print("Error, subrows of the matrix out of range.", file=sys.stderr)
        return
    if len(h[0]) < cols[-1] + 1:
        print("Error, subcolumns of the matrix out of range.", file=sys.stderr)
        return

    for col in cols:
        print(f"       |{col:2d}>  ", end='')
    print('\n', end='')

    flt_fmt = '+1.2f'
    empty = ' ' * 5
    for row in rows:
        print(f"<{row:2d}|", end='')
        for x in h[row][cols[0]:cols[-1]+1]:
            if abs(x.real) < 0.001:
                real = empty
            else:
                real = f'{x.real:{flt_fmt}}'

            if abs(x.imag) < 0.001:
                imag = empty
            else:
                imag = f'{x.imag:{flt_fmt}}'

            print(f"({real},{imag})", end='')
        print("\n", end='')


def print_matrix(h, title: str = ""):
    print(f"Printing : {title}")
    print('   ', end='')
    for i, row in enumerate(h):
        print(f"       |{i:2d}>  ", end='')
    print('\n', end='')

    flt_fmt = '+1.2f'
    empty = ' ' * 5
    for i, row in enumerate(h):
        print(f"<{i:2d}|", end='')
        for x in row:
            if abs(x.real) < 0.001:
                real = empty
            else:
                real = f'{x.real:{flt_fmt}}'

            if abs(x.imag) < 0.001:
                imag = empty
            else:
                imag = f'{x.imag:{flt_fmt}}'

            print(f"({real},{imag})", end='')
        print("\n", end='')


def print_states_positions(states):
    state_id2name = {}
    for state in states:
        irrep = state['irrep']
        multiplicity = state['multiplicity']
        pos = state['position']
        first = pos[0]
        last = pos[1]
        for n, p in enumerate(range(first, last)):
            # s > 0 by definition
            # spin_z goes from -s up to s
            # multiplicity is 2s+1
            # s = 0.5 * (multiplicity - 1)
            spin_z = - (multiplicity - 1) // 2 + n
            print(f"|{p:2d}> = |{irrep}, {multiplicity}, {spin_z}>")
            state_id2name[p] = {
                "irrep": irrep,
                "multiplicity": multiplicity,
                "spin_z": spin_z,
            }
    return state_id2name


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
        mel = np.array(soc['matrix'], dtype=np.cdouble)
        soc_matrix[bra_pos[0]:bra_pos[1], ket_pos[0]:ket_pos[1]] = mel
        mel_hc = np.conjugate(mel.T)
        soc_matrix[ket_pos[0]:ket_pos[1], bra_pos[0]:bra_pos[1]] = mel_hc

    return soc_matrix


def soc_max_helper(soc):
    matrix = soc['matrix']
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
        print(soc['matrix'])


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


LATEX_TABLE_HEADER = r"""
\begin{tabular}{|c|r|r|l|}
\hline
id & $E _{ex}$, cm$^{-1}$ & $E _{ex}$, eV & eigenvector \\
\hline"""

LATEX_TABLE_TAIL = r"""
\hline
\end{tabular}"""


LATEX_TABLE_HEADER_EXTRA = r"""
\begin{tabular}{|l|l|}
\hline
nickname & state \\
\hline"""


def deal_with_spectrum_printing(args, cols, evalues, evectors, state_id2name):

    if args.eigenvectors == "":
        return

    if 'l' in args.eigenvectors:
        print(LATEX_TABLE_HEADER_EXTRA)
        for col in cols:
            line = r'$\ket{' + f"{col:2d}" + r'}$'
            line += " & "
            line += "$"
            line += state2latex(state_id2name[col])
            line += "$"
            line += r' \\'
            print(line)
        print(LATEX_TABLE_TAIL)

    print("\n")
    if "l" in args.eigenvectors:
        print(LATEX_TABLE_HEADER)

    for id in cols:
        energy = evalues[id]
        vector = evectors[:, id]
        print_threshold = args.threshold
        vector_str = print_vector_latex(
            vector, polar=True, norm_threshold=print_threshold)
        if "a" in args.eigenvectors:
            print(f"{id:2d}: {energy:9.2f} cm-1"
                  f" = {energy*cm2eV:6.3f} eV"
                  f"\t\t{vector_str}")
        elif "l" in args.eigenvectors:
            print(f"{id:2d} & "
                  f"{energy:9.2f} & "
                  f"{energy*cm2eV:6.3f} & "
                  f"{vector_str} \\\\")

    if "l" in args.eigenvectors:
        print(LATEX_TABLE_TAIL)


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

    socs_ref2eom = data['ref2eom']
    socs_eom2eom = data['eom2eom']
    add_order_to_SOC(states, socs_ref2eom)
    add_order_to_SOC(states, socs_eom2eom)
    socs_aggregate = socs_ref2eom + socs_eom2eom

    hamiltonian = construct_Hamiltonian_matrix(dim, states, socs_aggregate)

    state_id2name = print_states_positions(states)

    rows, cols = prepare_subblock_ranges(args, dim)
    print_submatrix(hamiltonian, rows, cols, title="SOCs + diagonal energies")

    evalues, evectors = np.linalg.eigh(hamiltonian)

    deal_with_spectrum_printing(args, cols, evalues, evectors, state_id2name)

    if args.show_largest is True:
        find_largest_soc(socs_aggregate)


if __name__ == "__main__":
    main()
