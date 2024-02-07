# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca,Sr]/ECP10MDF[Ca]/ECP28MDF[Sr]
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

# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca,Sr]/cc-pVDZ[H,C,O]
# The 0/A1 singlet had to have its label changed to 1/A1 because the CCSD
# reference in here is the 1^1 A _1 state.
ref2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(-22.442424+0j)], [0j], [(-22.442424+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[(11.714511+0j)], [0j], [(11.714511+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'matrix': [[11.251557j], [0j], [-11.251557j]]
    }
]


# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca,Sr]/cc-pVDZ[H,C,O]
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
        'matrix': [[(-51.219402+0j)], [0j], [(-51.219402+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[(-2.839709+0j)], [0j], [(-2.839709+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'matrix': [[1.38023j], [0j], [-1.38023j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-50.219231+0j)], [0j], [(-50.219231+0j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(55.841937+0j)], [0j], [(55.841937+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'matrix': [[0j], [-3.691849j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(-10.922218+0j)], [0j], [(-10.922218+0j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(0.762187+0j)], [0j], [(0.762187+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/B1', 'multiplicity': 1},
        'matrix': [[0j], [26.386804j], [0j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[50.578888j], [0j], [(-0-50.578888j)]]
    },
    {
        'bra': {'irrep': '2/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[-55.902821j], [0j], [55.902821j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [94.385224j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [5.958423j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    }
]
