# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca,Sr]/ECP10MDF[Ca]/ECP28MDF[Sr]
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

# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca,Sr]/cc-pVDZ[H,C,O]
# The 0/A' singlet had to have its label changed to 1/A' because the CCSD
# reference in here is the 1^1 A ^' state.
ref2eom = [
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.173619j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [-41.428811j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [4.463352j], [0j]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[0j], [19.302869j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "1/A'", 'multiplicity': 1},
        'matrix': [[(-11.168595+4.07909j)], [0j], [(-11.168595-4.07909j)]]
    }
]


# EOM-EE-CCSD/RHF/aug-cc-pwCVDZ-X2C[Ca,Sr]/cc-pVDZ[H,C,O]
# The n/A' singlets had to have its label changed to (n+1)/A' as the CCSD
# reference in here is the 1^1 A ^' state.
eom2eom = [
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-70.287725j], [0j]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [-0.503914j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [-92.422685j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[0j], [14.362396j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "2/A'", 'multiplicity': 1},
        'matrix': [[(2.730499-8.842054j)], [0j], [(2.730499+8.842054j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[0j], [2.984762j], [0j]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[0j], [92.166171j], [0j]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[0j], [-0.125361j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[(-0+0j)], [-10.934617j], [0j]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "3/A'", 'multiplicity': 1},
        'matrix': [[(5.270093+2.63564j)], [0j], [(5.270093-2.63564j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [20.202046j], [0j]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.927101j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [4.707875j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[0j], [0.173218j], [(-0+0j)]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': "4/A'", 'multiplicity': 1},
        'matrix': [[(-10.591988-14.14238j)], [0j], [(-10.591988+14.14238j)]]
    },
    {
        'bra': {'irrep': "1/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(-45.200179-23.194291j)], [0j], [(-45.200179+23.194291j)]]
    },
    {
        'bra': {'irrep': "2/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(-37.165243+70.323244j)], [0j], [(-37.165243-70.323244j)]]
    },
    {
        'bra': {'irrep': "3/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(-57.432071-32.239625j)], [0j], [(-57.432071+32.239625j)]]
    },
    {
        'bra': {'irrep': "4/A'", 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[(12.748511-4.957622j)], [0j], [(12.748511+4.957622j)]]
    },
    {
        'bra': {'irrep': '1/A"', 'multiplicity': 3},
        'ket': {'irrep': '1/A"', 'multiplicity': 1},
        'matrix': [[0j], [0.097033j], [0j]]
    }
]
