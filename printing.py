"""
Set of scipts that help with picturing the SOC decoupling process
"""

import sys
import cmath as m

eV2cm = 8065.479
cm2eV = 1.0/eV2cm


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
    # handle fractional spins
    if (spin_z % 1 > 0.1):
        spin_z = r"\frac{" + str(int(2*spin_z)) + r"}{2}"
    else:
        spin_z = f"{int(spin_z):2d}"

    out = r'\ket{' + irrepN + ' ^{' + str(multiplicity) + '} '
    out += irrep_lttr + irrep_decorator + ', ' + spin_z + '}'
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
                # Positive number on the real axis
                if abs(phi) < 0.01:
                    output += f"+{norm:4.3f}"
                # Negative number on the real axis
                elif abs(phi) > 0.95 and abs(phi) < 1.05:
                    output += f"-{norm:4.3f}"
                # On the imaginary axis up
                elif phi > 0.45 and phi < 0.55:
                    output += f"+{norm:4.3f}i"
                # On the imaginary axis down
                elif phi < -0.45 and phi > -0.55:
                    output += f"-{norm:4.3f}i"
                # The number does not lie on any axis – need to show the phase
                else:
                    output += f"{norm:+4.3f}"
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
        elif norm**2 > 5e-4:
            small_contributions = True
    if small_contributions:
        output += r"+ \ldots"
    output += "$"

    # trim the leading + sign
    if output[1] == "+":
        output = "$" + output[2:]

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


def get_stateID_to_name_dict(states):
    stateID2name = {}
    for state in states:
        irrep = state['irrep']
        multiplicity = state['multiplicity']
        pos = state['position']
        e_ex_eV = state['energy']['E ex']['eV']
        first = pos[0]
        last = pos[1]
        for n, p in enumerate(range(first, last)):
            # s > 0 by definition
            # spin_z goes from -s up to s
            # multiplicity is 2s+1
            # s = 0.5 * (multiplicity - 1)
            spin_z = - (multiplicity - 1) / 2 + n
            # print(f"|{p:2d}> = |{irrep}, {multiplicity}, {spin_z}>")
            stateID2name[p] = {
                "irrep": irrep,
                "multiplicity": multiplicity,
                "spin_z": spin_z,
                "energy eV": e_ex_eV,
            }
    return stateID2name


# LATEX_TABLE_HEADER = r"""\begin{tabular}{|c|r|r|l|}
# \hline
# id & $E _{ex}$, cm$^{-1}$ & $E _{ex}$, eV & eigenvector \\
# \hline"""
LATEX_TABLE_HEADER_OLD = r"""\begin{tabular}{|c|r|l|}
\hline
id & $E _{ex}$, cm$^{-1}$ & eigenvector \\
\hline"""

LATEX_TABLE_TAIL = r"""\hline
\end{tabular}"""


LATEX_TABLE_HEADER_EXTRA = r"""
\begin{tabular}{|l|l|r|}
\hline
label & state & $E _{ex}$, cm$^{-1}$ \\
\hline"""


def deal_with_spectrum_printing_old(args, cols, evalues, evectors, states):
    """
    Prints the eigenvectors of the state interaction Hamiltonian.
    """

    if args.eigenvectors == "":
        return

    state_id2name = get_stateID_to_name_dict(states)

    if 'l' in args.eigenvectors:
        print(LATEX_TABLE_HEADER_EXTRA)
        for col in cols:
            line = r'$\ket{' + f"{col:2d}" + r'}$'
            line += " & "
            line += "$"
            line += state2latex(state_id2name[col])
            line += "$"
            line += " & "
            line += f"{state_id2name[col]['energy eV'] * eV2cm:9.2f}"
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
                  # f"{energy*cm2eV:6.3f} & "
                  f"{vector_str} \\\\")

    if "l" in args.eigenvectors:
        print(LATEX_TABLE_TAIL)


LATEX_TABLE_HEADER = r"""\begin{tabular}{|r|l|r|r|l|}
\hline
id &
EOM state &
$E _{ex}$&
$\Delta E ^{SOC}$&
SOC-corrected eigenvector \\
\hline"""


def deal_with_spectrum_printing(args, cols, evalues, evectors, states):
    """
    Prints the eigenvectors of the state interaction Hamiltonian.
    """

    if args.eigenvectors == "":
        return

    state_id2name = get_stateID_to_name_dict(states)

    if "l" in args.eigenvectors:
        print(LATEX_TABLE_HEADER)

    for id in cols:
        soc_energy = evalues[id]
        vector = evectors[:, id]
        print_threshold = args.threshold
        vector_str = print_vector_latex(
            vector, polar=True, norm_threshold=print_threshold)
        if "a" in args.eigenvectors:
            print(f"{id:2d}: {soc_energy:9.2f} cm-1"
                  f" = {soc_energy*cm2eV:6.3f} eV"
                  f"\t\t{vector_str}")
        elif "l" in args.eigenvectors:
            # ket's name
            line = r'$\ket{' + f"{id:2d}" + r'}$'
            line += " & "
            line += "$"
            line += state2latex(state_id2name[id])
            line += "$"
            line += " & "
            ref_energy = state_id2name[id]['energy eV'] * eV2cm
            line += f"{ref_energy:9.2f}"
            line += " & "
            soc_correction = soc_energy - ref_energy
            line += f"{soc_correction:9.2f} & "
            # line += f"{energy*cm2eV:6.3f} & "
            line += f"{vector_str} "
            line += r' \\'
            print(line)

    if "l" in args.eigenvectors:
        print(LATEX_TABLE_TAIL)


def print_branching_ratios(args, dim, evalues, soc_tdms_abs2):
    if args.branching_ratios is None:
        return

    higher_state_id = args.branching_ratios
    if higher_state_id < 0 or higher_state_id >= dim:
        print("Invalid value of argument of --branching_ratios "
              f"{higher_state_id}\n"
              f"Only values from the range [0, {dim}) are allowed.",
              file=sys.stderr)
        return 1

    state_energy = evalues[higher_state_id]
    einsteins_As = list()
    for lower_state_id in range(0, higher_state_id):
        gap = state_energy - evalues[lower_state_id]
        gap_cube = gap**3
        tdm_square = soc_tdms_abs2[higher_state_id, lower_state_id]
        einstein_A = gap_cube * tdm_square
        einsteins_As.append(einstein_A)

    einstein_As_sum = sum(einsteins_As)

    print(f"Braching ratios from state #{higher_state_id}")
    print("Lower state id, branching ratio, TDM^2 au , gap")
    for lower_state_id, a in enumerate(einsteins_As):
        tdm_square = soc_tdms_abs2[higher_state_id, lower_state_id]
        gap = state_energy - evalues[lower_state_id]
        print(f"{lower_state_id:14d}, "
              f"{a/einstein_As_sum:15.3f}, "
              f"{tdm_square:9.3f}, "
              f"{gap:7.1f}")
