# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca]/ECP10MDF[Ca]
states = [
    {"irrep": "1/Ag", "energy": {"E ex": {"eV": 0.0}}, "multiplicity": 1},
    # The CCSD convergence threshold is 2.7e-5 eV aka 1-6 Hartree
    {"irrep": "1/B3u", "energy": {"E ex": {"eV": 1.3e-5}}, "multiplicity": 3},
    {"irrep": "1/B1g", "energy": {"E ex": {"eV": 2.0438}}, "multiplicity": 1},
    {"irrep": "1/B2u", "energy": {"E ex": {"eV": 2.0438}}, "multiplicity": 3},
    {"irrep": "1/B2g", "energy": {"E ex": {"eV": 2.0600}}, "multiplicity": 1},
    {"irrep": "1/B1u", "energy": {"E ex": {"eV": 2.0600}}, "multiplicity": 3},
    {"irrep": "1/B2u", "energy": {"E ex": {"eV": 2.0660}}, "multiplicity": 1},
    {"irrep": "1/B1g", "energy": {"E ex": {"eV": 2.0660}}, "multiplicity": 3},
    {"irrep": "1/B1u", "energy": {"E ex": {"eV": 2.0848}}, "multiplicity": 1},
    {"irrep": "1/B2g", "energy": {"E ex": {"eV": 2.0848}}, "multiplicity": 3},
]

# EOM-EE-CCSD/RHF/def2TZVP
# The 0/Ag singlet had to have its label changed to 1/Ag because the CCSD
# reference in here is the 1^1 A _g state.
ref2eom = [
    {
        'bra': {'irrep': '1/B1g', 'multiplicity': 3},
        'ket': {'irrep': '1/Ag', 'multiplicity': 1},
        'matrix': [[0j], [-19.184544j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2g', 'multiplicity': 3},
        'ket': {'irrep': '1/Ag', 'multiplicity': 1},
        'matrix': [[(13.629352+0j)], [0j], [(13.629352+0j)]]
    },
    {
        'bra': {'irrep': '1/B1u', 'multiplicity': 3},
        'ket': {'irrep': '1/Ag', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2u', 'multiplicity': 3},
        'ket': {'irrep': '1/Ag', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B3u', 'multiplicity': 3},
        'ket': {'irrep': '1/Ag', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    }
]


# EOM-EE-CCSD/RHF/def2TZVP
eom2eom = [
    {
        'bra': {'irrep': '1/B1g', 'multiplicity': 3},
        'ket': {'irrep': '1/B1g', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2g', 'multiplicity': 3},
        'ket': {'irrep': '1/B1g', 'multiplicity': 1},
        'matrix': [[18.684462j], [0j], [(-0-18.684462j)]]
    },
    {
        'bra': {'irrep': '1/B1u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1g', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1g', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B3u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1g', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1g', 'multiplicity': 3},
        'ket': {'irrep': '1/B2g', 'multiplicity': 1},
        'matrix': [[18.690807j], [0j], [(-0-18.690807j)]]
    },
    {
        'bra': {'irrep': '1/B2g', 'multiplicity': 3},
        'ket': {'irrep': '1/B2g', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2g', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2g', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B3u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2g', 'multiplicity': 1},
        'matrix': [[(1e-06+0j)], [0j], [(1e-06+0j)]]
    },
    {
        'bra': {'irrep': '1/B1g', 'multiplicity': 3},
        'ket': {'irrep': '1/B1u', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2g', 'multiplicity': 3},
        'ket': {'irrep': '1/B1u', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1u', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1u', 'multiplicity': 1},
        'matrix': [[18.709665j], [0j], [(-0-18.709665j)]]
    },
    {
        'bra': {'irrep': '1/B3u', 'multiplicity': 3},
        'ket': {'irrep': '1/B1u', 'multiplicity': 1},
        'matrix': [[(18.290674+0j)], [0j], [(18.290674+0j)]]
    },
    {
        'bra': {'irrep': '1/B1g', 'multiplicity': 3},
        'ket': {'irrep': '1/B2u', 'multiplicity': 1},
        'matrix': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B2g', 'multiplicity': 3},
        'ket': {'irrep': '1/B2u', 'multiplicity': 1},
        'matrix': [[-1e-06j], [0j], [1e-06j]]
    },
    {
        'bra': {'irrep': '1/B1u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2u', 'multiplicity': 1},
        'matrix': [[-18.684213j], [0j], [18.684213j]]
    },
    {
        'bra': {'irrep': '1/B2u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2u', 'multiplicity': 1},
        'matrix': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B3u', 'multiplicity': 3},
        'ket': {'irrep': '1/B2u', 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-25.699812j], [0j]]
    }
]
