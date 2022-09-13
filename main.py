from env import Env
from modules.data_manipulate import EnergyAndDistances

input_file = Env.path_data
residue = 'FAD603'
fnq = 'F02'
mode = 'A'

print(f'Reading data from {input_file}...')
data = EnergyAndDistances(input_file)
# print(data.extract_energy_distances(residue))
print(f'Extracting {fnq}...')
#print(data.extract_distances())
#print(data.extract_distances_by_fnq(fnq))
#print(data.extract_distances_by_fnq_and_mode(fnq=fnq, mode=mode))
print(data.distances_in_interval_by_fnq(fnq,3, 5, 3))
#print(data.extract_energy_distances_by_residue('FAD603'))
#print(data.extract_energy_distances_by_residue_and_fnq(residue, fnq, 'GOL'))