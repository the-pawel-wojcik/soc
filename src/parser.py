#!/usr/bin/env python3

"""
This script reads the Q-Chem's output in serach of section which contain SOCs.
"""

import argparse
import re
import sys


def get_s_from_s2(s2: float) -> float:
    """
    <S^2> = s(s+1)
    --> s = 0.5 * ( -1 + sqrt(1 + 4 <S^2>) )

    Input:
        s2: float: <S^2>

    Returns:
        s: float
    """

    return 0.5 * (-1 + pow(1 + 4 * s2, 0.5))


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('qchem_output')
    args = parser.parse_args()
    return args


def skip_to(what: str, lines, ln: int):
    """ Skip to the line that matches `what`.
        Returns:
            `ln` int: number of the line where the match was found
    """
    pattern = re.compile(what)
    while True:
        match = pattern.match(lines[ln].strip())
        if match is not None:
            break
        ln += 1
        if ln >= len(lines):
            raise RuntimeError(f"Error in parsing. Did not find:\n{what}")

    return ln


def get_trans_props(qchem: list[str]) -> list[list[str]]:
    trans_props = []

    property = None  # list[str] this variable stores transition property lines
    for ln, line in enumerate(qchem):

        # There is a new property detected
        if line.strip().startswith('State A:'):
            # This can be the first one
            if property is None:
                property = [line]
                continue
            # Or it might be a new one
            trans_props += [property]
            property = [line]
            continue
        # Just another line
        else:
            # If no properties start was detected yet
            if property is None:
                continue
            # There was a property detected already
            property += [line]

    # Save the last property if any was detected
    if property is not None:
        trans_props += [property]

    return trans_props


def parse_SOC_section(prop: list[str]) -> dict | None:
    data = {}
    ln = 0
    content = prop[ln]
    sep_start = content.find(':')
    state_A = content[sep_start + 1:].strip()
    ln += 1
    content = prop[ln]
    sep_start = content.find(':')
    state_B = content[sep_start + 1:].strip()

    data['State A'] = {'name': state_A}
    data['State B'] = {'name': state_B}

    try:
        ln = skip_to(r"\s*Transition dipole moment", prop, ln)
    except Exception:
        print("Error while parsing transition:", file=sys.stderr)
        print(f"\tState A: {state_A}", file=sys.stderr)
        print(f"\tState B: {state_B}", file=sys.stderr)
        return None

    # tdm = transition dipole moment
    # Q-Chem reports tdms for pairs of states
    # what I call B_tdm_A is in Q-Chem labelled as A->B
    # and what I call A_tdm_B in Q-Chem is called B->A
    # these must correspond to:
    # <state_A| d | state_B> and <state_B| d |state_A>
    # but I don't know which one is which.

    # In the SOC-section the A->B convention corresponds to
    # <state_B| H_BP | state_A>
    # consequently I stick to this convention also in the
    # scalar values, hoping that Q-Chem output convention is consistent.

    # These two values can differ a bit bc in the EOM theory
    # the left and right eigenvectors are different
    # so some sort of averaging is necessary to get a single value

    ln += 1
    content = prop[ln].split()
    B_tdm_A = float(content[1])
    vec_B_tdm_A = dict()
    vec_B_tdm_A["x"] = float(content[3][:-1])  # [:-1] trailing comma
    vec_B_tdm_A["y"] = float(content[5][:-1])  # [:-1] trailing comma
    vec_B_tdm_A["z"] = float(content[7][:-1])  # [:-1] trailing ")"

    ln += 1
    content = prop[ln].split()
    A_tdm_B = float(content[1])
    vec_A_tdm_B = dict()
    vec_A_tdm_B["x"] = float(content[3][:-1])  # [:-1] trailing comma
    vec_A_tdm_B["y"] = float(content[5][:-1])  # [:-1] trailing comma
    vec_A_tdm_B["z"] = float(content[7][:-1])  # [:-1] trailing ")"

    # the geometric average of the left and right tdms
    # TODO: remove the averaging from here:
    # The parser should only read the input. Any post-processing
    # like finding the averaged tdm should be separated from parsing.

    tdm = pow(B_tdm_A * A_tdm_B, 0.5)
    data["tdm"] = tdm

    # arithmetic average of their components
    vec_tdm = dict()
    for xyz in vec_B_tdm_A.keys():
        vec_tdm[xyz] = 0.5 * (vec_B_tdm_A[xyz] + vec_A_tdm_B[xyz])

    data["vec tdm"] = vec_tdm
    data["vec B_tdm_A"] = vec_B_tdm_A
    data["vec A_tdm_B"] = vec_A_tdm_B

    ln = skip_to(r"Oscillator strength", prop, ln)
    content = prop[ln].split()
    f = float(content[-1])
    data["f"] = f

    """
    Matrices of spin-orbit couplings
    """
    # # TODO: here are some available errors
    # soc_text_left = "A(Ket)->B(Bra) transition SO matrices"
    # soc_error = "I am going to skip this transition"
    # soc_fatal_error = "Failed to compute integrals!"
    # yellow_flag = False
    # red_flag = False
    # # TODO: instead of while use skip_to_line_starting_with
    # # and add the possible error messages as new functionality
    # while True:
    #     next_line = self.parent.get_line().strip()
    #     if next_line.startswith(soc_error):
    #         yellow_flag = True
    #         break
    #     if next_line.startswith(soc_fatal_error):
    #         red_flag = True
    #         break
    #     if next_line.startswith(soc_text_left):
    #         break
    # if yellow_flag:
    #     print("The SOC calculations were unsuccessfull!")
    #     print(f"Q-Chem skipped transition {state_A} ", end='')
    #     print(f"-> {state_B}.")
    #     print("Check the output file.")
    #     print(f"Current input file line is {self.parent.input_line}")
    #     self.soc_invalid = True

    # if red_flag:
    #     print("The SOC failed to compute intergrals!")
    #     print("Try adding in the input")
    #     print("\tqints_soc_mem = 3000")
    #     print("Large basis sets might require more memory.")
    #     print("Make sure that cc_memory and qints_soc_memory"
    #           "don't exceed total memory.")
    #     self.soc_invalid = True

    # SOC A(ket) -> B(bra), i.e., <B| H_SO |A>
    try:
        ln = skip_to(r'\s*A\(Ket\)->B\(Bra\) transition SO matrices', prop, ln)
    except Exception:
        print("No SOCs in output for transition:", file=sys.stderr)
        print(f"\tState A: {state_A}", file=sys.stderr)
        print(f"\tState B: {state_B}", file=sys.stderr)
        return None

    FLOAT = r'([+-]?\d+\.\d+)'
    braket_re = r"\s*(?:Ket|Bra) state:  Computed S\^2 = " + FLOAT + \
        " will be treated as " + FLOAT + " Sz = " + FLOAT
    braket_pattern: re.Pattern = re.compile(braket_re)
    # Some version of Q-Chem have a different number of lines
    ln = skip_to(r'\s*Ket state:  Computed S\^2 =.*', prop, ln)
    match = braket_pattern.match(prop[ln])
    ket_s2 = float(match.group(2))
    ket_s = get_s_from_s2(ket_s2)
    ket_dim = int(2 * ket_s) + 1
    data['State A']['<S^2>'] = ket_s2
    data['State A']['multiplicity'] = ket_dim
    ln += 1
    match = braket_pattern.match(prop[ln])
    bra_s2 = float(match.group(2))
    bra_s = get_s_from_s2(bra_s2)
    bra_dim = int(2 * bra_s) + 1
    data['State B']['<S^2>'] = bra_s2
    data['State B']['multiplicity'] = bra_dim
    ln += 1
    content = prop[ln].split()[-1]
    if content == "0.000":
        print("No SOC available for the transition:", file=sys.stderr)
        print(f"  State A: {state_A}", file=sys.stderr)
        print(f"  State B: {state_B}", file=sys.stderr)
        return None

    try:
        ln = skip_to(r'\s*Mean-field SO', prop, ln)
    except Exception:
        print("Error while parsing transition:", file=sys.stderr)
        print(f"\tState A: {state_A}", file=sys.stderr)
        print(f"\tState B: {state_B}", file=sys.stderr)
        return None
    ln += 7
    # ket_re = r'|Sz=(\d\.\d\d\)>'
    # ket_pattern = re.compile(ket_re)
    # matches = ket_pattern.findall(prop[ln])
    matrix = [[0.0 + 0.0j for _ in range(ket_dim)] for _ in range(bra_dim)]
    for row_number, row in enumerate(range(bra_dim)):
        ln += 1
        content = prop[ln].strip()
        content = content.split('|')[1]
        vals = content.split(')(')
        vals[0] = vals[0][1:]  # remove the inital (
        vals[-1] = vals[-1][:-1]  # remove the terminal )
        for column_number, value in enumerate(vals):
            (real_part, imag_part) = value.split(',')
            real_part = float(real_part)
            imag_part = float(imag_part)
            matrix[row_number][column_number] = real_part + 1.0j * imag_part

    data["SOC"] = {"<B|H _SO|A>": matrix}
    return data


def print_summary_of_transitions(transition_props):
    for props in transition_props:
        print(f"State A: {props['State A']}")
        print(f"State B: {props['State B']}")
        print(f"A: <S^2> = {props['S^2 A']:.2f} multiplicity ="
              f" {props['multiplicity A']}")
        print(f"B: <S^2> = {props['S^2 B']:.2f} multiplicity ="
              f" {props['multiplicity B']}")
        print("SOC")
        soc = props['SOC']
        print(f"<{soc['<bra|']}| H _SO |{soc['|ket>']}>")
        print(soc['matrix'])
        print("\n")


def pretty_print_eom2eom(transitions):
    TAB = '\t'
    print("eom2eom = [")
    for transition in transitions:
        print(TAB, "{")
        for key, val in transition.items():
            print(TAB*2, f'"{key}": {val},')
        print(TAB, "},")
    print("]")


def main():
    """ An example of a q-chem output block that this script parses:
 ------------------------------------------------------------------------------
 State A: ccsd: 0/A1
 State B: eomee_ccsd/rhfref/triplets: 1/A1
 Energy GAP = 0.168 a.u. = 4.574 eV
 Transition dipole moment (a.u.):
   A->B: 0.000000 (X 0.000000, Y 0.000000, Z 0.000000)
   B->A: 0.000000 (X 0.000000, Y 0.000000, Z 0.000000)
 Oscillator strength (a.u.): 0.000000
 Transition angular momentum against gauge origin (a.u.):
   A->B:  (X 0.000000i, Y 0.000000i, Z 0.000000i)
   B->A:  (X 0.000000i, Y 0.000000i, Z 0.000000i)
 Norm of one-particle transition density matrix:
   A->B: 0.503932;   B->A: 0.993439
   ||gamma^AB||*||gamma^BA||: 0.500626

 ______________________________________________________________
 A(Ket)->B(Bra) transition SO matrices
Full 2e SOC is not implemented withing libqints. 
I will do mean-field SOC with libqints, which is usually as good as full 2e SOC
 Analysing Sz ans S^2 of the pair of states...
 Ket state:  Computed S^2 = 0.000000 will be treated as 0.000000 Sz = 0.000000
 Bra state:  Computed S^2 = 2.000000 will be treated as 2.000000 Sz = 0.000000
 Clebsh-Gordan coefficient: <0.000,0.000;1.000,0.000|1.000,0.000> = 1.000
 _________________________________________________
 One-electron SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S'> = (0.000000,0.000000)
 <S|| Hso(L0) ||S'> = (0.000000,-0.000000)
 <S|| Hso(L+) ||S'> = (0.000000,-0.000000)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=0.00>
 <Sz=-1.00|(0.000000,-0.000000)
 <Sz=0.00|(0.000000,-0.000000)
 <Sz=1.00|(0.000000,0.000000)
 _________________________________________________
 Mean-field SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S'> = (0.000000,0.000000)
 <S|| Hso(L0) ||S'> = (0.000000,-0.000000)
 <S|| Hso(L+) ||S'> = (0.000000,-0.000000)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=0.00>
 <Sz=-1.00|(0.000000,-0.000000)
 <Sz=0.00|(0.000000,-0.000000)
 <Sz=1.00|(0.000000,0.000000)
 Singlet part of <S|| Hso(L0) ||S'> = (-0.000000,0.000000) (excluded from all matrix elements)
 L-/L+ Averaged reduced matrix elements:
 <S|| Hso(L-) ||S'> = (0.000000,0.000000)
 <S|| Hso(L+) ||S'> = (0.000000,-0.000000)
 ______________________________________________________________
 B(Ket)->A(Bra) transition SO matrices
Full 2e SOC is not implemented withing libqints. 
I will do mean-field SOC with libqints, which is usually as good as full 2e SOC
 Analysing Sz ans S^2 of the pair of states...
 Ket state:  Computed S^2 = 2.000000 will be treated as 2.000000 Sz = 0.000000
 Bra state:  Computed S^2 = 0.000000 will be treated as 0.000000 Sz = 0.000000
 Clebsh-Gordan coefficient: <1.000,0.000;1.000,0.000|0.000,0.000> = 0.577
 _________________________________________________
 One-electron SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S'> = (-0.000000,-0.000000)
 <S|| Hso(L0) ||S'> = (0.000000,0.000000)
 <S|| Hso(L+) ||S'> = (-0.000000,0.000000)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(0.000000,0.000000)(0.000000,0.000000)(0.000000,-0.000000)
 _________________________________________________
 Mean-field SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S'> = (-0.000000,-0.000000)
 <S|| Hso(L0) ||S'> = (0.000000,0.000000)
 <S|| Hso(L+) ||S'> = (-0.000000,0.000000)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(0.000000,0.000000)(0.000000,0.000000)(0.000000,-0.000000)
 Singlet part of <S|| Hso(L0) ||S'> = (-0.000000,-0.000000) (excluded from all matrix elements)
 L-/L+ Averaged reduced matrix elements:
 <S|| Hso(L-) ||S'> = (-0.000000,-0.000000)
 <S|| Hso(L+) ||S'> = (-0.000000,0.000000)
 ______________________________________________________________
   Arithmetically averaged transition SO matrices
   (The phases shown, Ket and Bra assingment are from A(Ket)->B(Bra))
 _________________________________________________
 One-electron SO (cm-1)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=0.00>
 <Sz=-1.00|(0.000000,-0.000000)
 <Sz=0.00|(0.000000,-0.000000)
 <Sz=1.00|(0.000000,0.000000)
 _________________________________________________
 Mean-field SO (cm-1)
 SOCC = 0.000000
 Actual matrix elements:
       |Sz=0.00>
 <Sz=-1.00|(0.000000,-0.000000)
 <Sz=0.00|(0.000000,-0.000000)
 <Sz=1.00|(0.000000,0.000000)
 ______________________________________________________________
"""
    args = get_args()
    with open(args.qchem_output) as qchem:
        trans_props_lines = get_trans_props(qchem)

    transition_props = []
    for prop in trans_props_lines:
        transition = parse_SOC_section(prop)
        if transition is None:
            continue
        transition_props += [transition]

    out_data = []
    for transition in transition_props:
        soc = transition['SOC']
        bra = transition['State B']
        ket = transition['State A']
        matrix = soc['<B|H _SO|A>']
        tdm = transition['vec B_tdm_A']
        out_data += [
            {
                'bra': {
                    'irrep': bra['name'].split()[-1],
                    'multiplicity': bra['multiplicity'],
                },
                'ket': {
                    'irrep': ket['name'].split()[-1],
                    'multiplicity': ket['multiplicity'],
                },
                'H SO': matrix,
                'tdm': tdm,
            },
        ]

    pretty_print_eom2eom(out_data)


if __name__ == "__main__":
    main()
