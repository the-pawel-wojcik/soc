# Resolve spin-orbit states in electronic transitions
Programs like Q-Chem calculate eigenstates of the electronic Hamiltonian and
their various properties, like spin-orbit couplings. This program takes the
Q-Chem's output, extracts from it the valuable numbers, and assembles a
"state-interaction" Hamiltonian, diagonalises the Hamiltonian to produce the
spin-orbit corrected states, and finally prints out the spin-orbit corrected
properties, like excitation energies or transition dipole moments.

## Tutorial

### Collect spin-orbit couplings and transition dipole moments
```bash
parser.py soc.inp.out > input_data.py
```
The `input_data.py` file is unformatted. You might use the `useful_macros.vim`
for help with formatting it, should you wish to look at it.

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

### Collected electronic states
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

Warning: if the SOC calculations involve the CC reference, watch out for the
repeating irrep labels.

### Collected state dipole moments
The list `eom2eom` needs to be extended by "diagonal" entries with state dipole
moments. It is only needed for proper account of the transition dipole moments.
The `pqc/dipole_moments.py` script can do it.

### Assemble and diagonalize the Hamiltonian
Finally. Use the `soc.py` script to construct and diagonalize both the
Hamiltonian and the dipole moment matrices. By default the script does not
print anything. See the help flag `--help` for listing of all options.
```bash
python src/soc.py --help
```
Show SOC-corrected energies and eigenvalues
```bash
python src/soc.py examples/input_data.py -e a
# or if you would like to see it as a latex table
python src/soc.py examples/input_data.py -e l
```
Show the full Hamiltonian (ASCII art)
```bash
python src/soc.py examples/input_data.py -H
```
Show the full Hamiltonian as matplotlib plot
```bash
python src/soc.py examples/input_data.py -p H
python src/soc.py examples/input_data.py -p t  # view the dipole matrices
```

## Other files
`plt_soc.py` and `printing.py` are "libraries" with helper scripts.
