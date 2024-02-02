# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca]/ECP10MDF[Ca]
states = [
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 0.0}}, "multiplicity": 1},
    # The CCSD convergence threshold is 2.7e-5 eV aka 1-6 Hartree
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 1.4e-6}}, "multiplicity": 3},
    {"irrep": "1/B1", "energy": {"E ex": {"eV": 1.6265}}, "multiplicity": 1},
    {"irrep": "1/B1", "energy": {"E ex": {"eV": 1.6265}}, "multiplicity": 3},
    {"irrep": "1/B2", "energy": {"E ex": {"eV": 1.6555}}, "multiplicity": 1},
    {"irrep": "1/B2", "energy": {"E ex": {"eV": 1.6555}}, "multiplicity": 3},
    {"irrep": "2/A1", "energy": {"E ex": {"eV": 1.9165}}, "multiplicity": 1},
    {"irrep": "2/A1", "energy": {"E ex": {"eV": 1.9175}}, "multiplicity": 3},
    {"irrep": "2/B1", "energy": {"E ex": {"eV": 2.0710}}, "multiplicity": 1},
    {"irrep": "2/B1", "energy": {"E ex": {"eV": 2.0710}}, "multiplicity": 3},

]

# EOM-EE-CCSD/RHF/def2TZVP
# The 0/A1 singlet had to have its label changed to 1/A1 because the CCSD
# reference in here is the 1^1 A _1 state.
ref2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]],
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]],
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(0.01921+0j)], [0j], [(0.01921+0j)]],
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(-10.645115+0j)], [0j], [(-10.645115+0j)]],
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[-0.017316j], [0j], [0.017316j]],
    }
]


# EOM-EE-CCSD/RHF/def2TZVP
# The n/A1 singlets had to have its label changed to (n+1)/A1 as the CCSD
# reference in here is the 1^1 A _1 state.
eom2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-2.019211+0j)], [0j], [(-2.019211+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-0.034379+0j)], [0j], [(-0.034379+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[1.948883j], [0j], [(-0-1.948883j)]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-0.037241+0j)], [0j], [(-0.037241+0j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-1.914315+0j)], [0j], [(-1.914315+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [-2.210965j], [0j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(-10.187451+0j)], [0j], [(-10.187451+0j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(0.08888+0j)], [0j], [(0.08888+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0.82626j], [0j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[(-0-0.061289j)], [0j], [0.061289j]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[1.846341j], [0j], [(-0-1.846341j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [2.227959j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [1.359509j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    }
]
