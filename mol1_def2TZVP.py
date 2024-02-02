states = [
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 0.0}}, "multiplicity": 1},
    # The CCSD convergence threshold is 2.7e-5 eV aka 1-6 Hartree
    {"irrep": "1/B1", "energy": {"E ex": {"eV": 1.68e-5}}, "multiplicity": 3},
    {"irrep": "1/B1", "energy": {"E ex": {"eV": 2.0354}}, "multiplicity": 1},
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 2.0356}}, "multiplicity": 3},
    {"irrep": "1/B2", "energy": {"E ex": {"eV": 2.0576}}, "multiplicity": 3},
    {"irrep": "1/A2", "energy": {"E ex": {"eV": 2.0577}}, "multiplicity": 1},
    {"irrep": "2/A1", "energy": {"E ex": {"eV": 2.0845}}, "multiplicity": 1},
    {"irrep": "2/B1", "energy": {"E ex": {"eV": 2.0847}}, "multiplicity": 3},
    {"irrep": "1/B2", "energy": {"E ex": {"eV": 2.0972}}, "multiplicity": 1},
    {"irrep": "1/A2", "energy": {"E ex": {"eV": 2.0973}}, "multiplicity": 3},
]


# EOM-EE-CCSD/RHF/def2TZVP
# The 0/A1 singlet had to have its label changed to 1/A1 as the CCSD
# reference in here is the 1^1 A _1 state.
ref2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[0j], [16.912039j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(0.012218+0j)], [0j], [(0.012218+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(-13.674327+0j)], [0j], [(-13.674327+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(-0-6.722041j)], [0j], [6.722041j]]
    }
]


# EOM-EE-CCSD/RHF/VTZ
# The n/A1 singlets had to have its label changed to (n+1)/A1 as the CCSD
# reference in here is the 1^1 A _1 state.
eom2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[0j], [13.809052j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-18.337882+0j)], [0j], [(-18.337882+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-1.089118+0j)], [0j], [(-1.089118+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[16.112341j], [0j], [-16.112341j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-14.246097j], [0j]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'matrix': [[9.075135j], [0j], [-9.075135j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'matrix': [[16.725476j], [0j], [-16.725476j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'matrix': [[(0.045373+0j)], [0j], [(0.045373+0j)]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(0.446873+0j)], [0j], [(0.446873+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-0-16.306634j)], [0j], [16.306634j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-13.657453j], [0j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[15.958409j], [0j], [-15.958409j]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[(-0.054546+0j)], [0j], [(-0.054546+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [22.649111j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-12.467911j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    }
]
