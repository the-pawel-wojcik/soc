# Resolve spin-orbit states in electronic transitions
## Usage
Use this script like this:
```bash
parser.py soc.inp.out > input_data.py
```
The `input_data.py` file is unformatted. You might use the `useful_macros.vim`
for help with formatting it.

The `input_data.py` file is a python script that will get executed to in order
to introduce the `eom2eom` variable in the processing script. For this reason
you need to decorate the relevant arrays with
```python
# EOM-EA-CCSD/RHF/cc-pVDZ
eom2eom = [
...
]
```
or something alike.

The `input_data.py` also needs the `states` list. Example:
```python
# EOM-DEA-CCSD/cc-pVDZ[H,C,O]/aug-cc-pVDZ-PP[Ca]/ECP10MDF[Ca]
states = [
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 0.0}}, "multiplicity": 1},
    {"irrep": "1/B1", "energy": {"E ex": {"eV": 2.0354}}, "multiplicity": 1},
    {"irrep": "1/A1", "energy": {"E ex": {"eV": 2.0356}}, "multiplicity": 3},
    {"irrep": "1/B2", "energy": {"E ex": {"eV": 2.0576}}, "multiplicity": 3},
]
```
The `pqc/energy.py` script is of help here. 

Warning: if the SOC calculations involve the CC referece, watch out for the
repeating irrep lables.

Finally. Use the `soc.py` script to construct and diagonalize both the
Hamiltonian and the dipole moment matrices. By default the script does not
print anything. See the help flag `-h` for details on how to use this script.

## Other files
`plt_soc.py` and `printing.py` are "libraries" with helper scripts.
