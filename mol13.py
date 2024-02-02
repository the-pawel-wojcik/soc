# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca]/ECP10MDF[Ca]
states = [
    {"irrep": "1/A'", "energy": {"E ex": {"eV": 0.0}}, "multiplicity": 1},
    {"irrep": "1/A'", "energy": {"E ex": {"eV": 0.0003}}, "multiplicity": 3},
    {"irrep": "2/A'", "energy": {"E ex": {"eV": 1.7618}}, "multiplicity": 1},
    {"irrep": "2/A'", "energy": {"E ex": {"eV": 1.7622}}, "multiplicity": 3},
    {"irrep": '1/A"', "energy": {"E ex": {"eV": 1.7838}}, "multiplicity": 3},
    {"irrep": '1/A"', "energy": {"E ex": {"eV": 1.7839}}, "multiplicity": 1},
    {"irrep": "3/A'", "energy": {"E ex": {"eV": 2.0443}}, "multiplicity": 1},
    {"irrep": "3/A'", "energy": {"E ex": {"eV": 2.0453}}, "multiplicity": 3},
    {"irrep": "4/A'", "energy": {"E ex": {"eV": 2.0652}}, "multiplicity": 1},
    {"irrep": "4/A'", "energy": {"E ex": {"eV": 2.0655}}, "multiplicity": 3},
]

# EOM-EE-CCSD/RHF/def2TZVP
# The 0/A' singlet had to have its label changed to 1/A' because the CCSD
# reference in here is the 1^1 A ^' state.
ref2eom = [
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.019213j], [0j]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [1.257406j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [13.916244j], [0j]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-3.430208j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[(-0.430196+0.619164j)], [0j], [(-0.430196-0.619164j)]]
    }
]


# EOM-EE-CCSD/RHF/def2TZVP
# The n/A' singlets had to have its label changed to (n+1)/A' as the CCSD
# reference in here is the 1^1 A ^' state.
eom2eom = [
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [1.343235j], [0j]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [-0.043751j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.783831j], [0j]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-3.552924j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[(-0.997743+1.532266j)], [0j], [(-0.997743-1.532266j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[0j], [-15.873123j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0.601721j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.305392j], [0j]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [1.260335j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[(0.853207+1.452444j)], [0j], [(0.853207-1.452444j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [-0.464176j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [3.48597j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.514096j], [0j]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.244976j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[(-2.143124-1.061888j)], [0j], [(-2.143124+1.061888j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(0.36286-0.718903j)], [0j], [(0.36286+0.718903j)]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(-1.035199+1.551701j)], [0j], [(-1.035199-1.551701j)]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(1.180178+1.747713j)], [0j], [(1.180178-1.747713j)]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(-2.006465-0.654059j)], [0j], [(-2.006465+0.654059j)]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[0j], [-0.064917j], [(-0+0j)]]
    }
]
