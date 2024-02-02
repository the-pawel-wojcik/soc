#!/usr/bin/env python3

"""
Created on Jan 29th 2024 by Paweł Wójcik.
The purpose of this script is to find the impact of SOCs on the spectrum of a
molecule.
"""

import sys
import numpy as np
import mol1_def2TZVP as mol1
import cmath as m

eV2cm = 8065.479
cm2eV = 1.0/eV2cm


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
    for coeff in vector:
        norm = abs(coeff[1])
        if norm > norm_threshold:
            output += "$"
            if polar:
                phi = m.phase(coeff[1]) / m.pi
                output += f"{norm:4.3f}"
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
            output += "$ "
            if polar:
                output += "+ "
        elif norm > 1e-16:
            small_contributions = True
    if small_contributions:
        if polar:
            output += r"\ldots "
        else:
            output += r"$+$ \ldots "
    return output


def print_matrix_simpler(h, title: str = ""):
    print(f"Printing : {title}")
    print('    ', end='')
    for i, row in enumerate(h):
        print(f"       {i:2d}  ", end='')
    print('\n', end='')

    flt_fmt = '+1.2f'
    for i, row in enumerate(h):
        print(f"{i:2d}: ", end='')
        for x in row:
            if abs(x.real) < 0.001:
                if abs(x.imag) < 0.001:
                    print("(     ,     )", end='')
                else:
                    print(f"(     ,{x.imag:{flt_fmt}})", end='')
            elif abs(x.imag) < 0.001:
                print(f"({x.real:{flt_fmt}},     )", end='')
            else:
                print(f"({x.real:{flt_fmt}},{x.imag:{flt_fmt}})", end='')
        print("\n", end='')


def print_matrix(h, title: str = ""):
    print(f"Printing : {title}")
    print('   ', end='')
    for i, row in enumerate(h):
        print(f"       |{i:2d}>  ", end='')
    print('\n', end='')

    flt_fmt = '+1.2f'
    for i, row in enumerate(h):
        print(f"<{i:2d}|", end='')
        for x in row:
            if abs(x.real) < 0.001:
                if abs(x.imag) < 0.001:
                    print("(     ,     )", end='')
                else:
                    print(f"(     ,{x.imag:{flt_fmt}})", end='')
            elif abs(x.imag) < 0.001:
                print(f"({x.real:{flt_fmt}},     )", end='')
            else:
                print(f"({x.real:{flt_fmt}},{x.imag:{flt_fmt}})", end='')
        print("\n", end='')


def print_states_positions(states):
    for state in states:
        irrep = state['irrep']
        multiplicity = state['multiplicity']
        pos = state['position']
        first = pos[0]
        last = pos[1]
        for p in range(first, last):
            print(f"|{p:2d}> = |{irrep}, {multiplicity}>")


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
        print(f"{bra_pos=}")
        print(f"{ket_pos=}")
        print(f"{mel=}")
        print(f"{mel_hc=}")

    print_states_positions(states)
    print_matrix(soc_matrix, title="SOCs + diagonal energies")
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


def main():
    states = mol1.states
    dim = introduce_order(states)
    socs_ref2eom = mol1.ref2eom
    socs_eom2eom = mol1.eom2eom
    add_order_to_SOC(states, socs_ref2eom)
    add_order_to_SOC(states, socs_eom2eom)
    socs_aggregate = socs_ref2eom + socs_eom2eom
    hamiltonian = construct_Hamiltonian_matrix(dim, states, socs_aggregate)
    evalues, evectors = np.linalg.eigh(hamiltonian)
    for n, e in enumerate(evalues):
        print(f"{e:9.3f} cm-1"
              f" = {e*cm2eV:6.3f} eV"
              f"\t\t{print_vector_latex(evectors[:, n], polar=True)}")

    find_largest_soc(socs_aggregate)
    # for i, v in enumerate(evectors[:, 2]):
    #     if abs(v) > 0.1:
    #         print(f"{i:2d}: {v.real:+.2f}{v.imag:+.2f}i")
    #     else:
    #         print(f"{i:2d}: 0")


if __name__ == "__main__":
    main()
