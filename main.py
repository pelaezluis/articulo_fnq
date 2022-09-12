from env import Env
from modules.data_manipulate import EnergyAndDistances

input_file = Env.path_data
residue = 'FAD603'
fnq = 'F02'
mode = 'Ap'

print(f'Reading data from {input_file}...')
data = EnergyAndDistances(input_file)
# print(data.extract_energy_distances(residue))
print(f'Extracting {fnq}...')
print(data.extract_energy_distances_by_residue_and_fnq(residue, fnq))