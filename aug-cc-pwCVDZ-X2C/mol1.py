# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca]/ECP10MDF[Ca]
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


# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca]/cc-pVDZ[H,C,O]
# The 0/A1 singlet had to have its label changed to 1/A1 as the CCSD
# reference in here is the 1^1 A _1 state.
ref2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'H SO': [[(-0+0j)], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'H SO': [[(-0+0j)], [16.371593j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'H SO': [[(-0.00804+0j)], [0j], [(-0.00804+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'H SO': [[(-13.256138+0j)], [0j], [(-13.256138+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A1', 'multiplicity': 1},
        'H SO': [[6.499042j], [0j], [(-0-6.499042j)]]
    }
]


# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca]/cc-pVDZ[H,C,O]
# The n/A1 singlets had to have its label changed to (n+1)/A1 as the CCSD
# reference in here is the 1^1 A _1 state.
eom2eom = [
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'H SO': [[0j], [0j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'H SO': [[0j], [13.342237j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'H SO': [[(-17.994614+0j)], [0j], [(-17.994614+0j)]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'H SO': [[(-1.210993+0j)], [0j], [(-1.210993+0j)]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '2/A1', 'multiplicity': 1},
        'H SO': [[15.384104j], [0j], [-15.384104j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'H SO': [[0j], [13.948085j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'H SO': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'H SO': [[8.864022j], [0j], [-8.864022j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'H SO': [[16.017607j], [0j], [-16.017607j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/A2', 'multiplicity': 1},
        'H SO': [[(0.038038+0j)], [0j], [(0.038038+0j)]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'H SO': [[(-0.690858+0j)], [0j], [(-0.690858+0j)]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'H SO': [[(-0-15.598686j)], [0j], [15.598686j]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'H SO': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'H SO': [[0j], [0j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B1', 'multiplicity': 1},
        'H SO': [[0j], [-13.077342j], [0j]]
    },
    {
        'bra': {'irrep': '1/A1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'H SO': [[15.157777j], [0j], [-15.157777j]]
    },
    {
        'bra': {'irrep': '1/A2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'H SO': [[(0.063802+0j)], [0j], [(0.063802+0j)]]
    },
    {
        'bra': {'irrep': '1/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'H SO': [[0j], [-22.136392j], [0j]]
    },
    {
        'bra': {'irrep': '2/B1', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'H SO': [[(-0+0j)], [11.854396j], [0j]]
    },
    {
        'bra': {'irrep': '1/B2', 'multiplicity': 3},
        'ket': {'irrep': '1/B2', 'multiplicity': 1},
        'H SO': [[(-0+0j)], [0j], [0j]]
    }
]
