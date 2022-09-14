import pandas as pd
import matplotlib.pyplot as plt
from env import Env
from os.path import join
from modules.data_manipulate import EnergyAndDistances

input_file = Env.path_data
output_matix_intervals = join(Env.path_save_data, 'matrix_intervals_params.csv')
residue = 'FAD603'
fnq = 'F17'
mode = 'A'

print(f'Reading data from {input_file}...')
data = EnergyAndDistances(input_file)
# print(data.extract_energy_distances(residue))
#print(f'Extracting {fnq}...')
#print(data.extract_distances())
#print(data.extract_distances_by_fnq(fnq))
#print(data.extract_distances_by_fnq_and_mode(fnq=fnq, mode=mode))
#print(data.distances_in_interval_by_fnq(fnq,3, 5, 1))
#print(data.extract_energy_distances_by_residue('FAD603'))
#print(data.extract_energy_distances_by_residue_and_fnq(residue, fnq, 'GOL'))
#print(data.fnq_list())

# CREAR MATRIX DE INTERVALOS
df_intervals = data.matrix_interval_distance(3, 5, output_matix_intervals)
df_intervals.plot.bar(x='Parameters', y=df_intervals.iloc[1:].columns)

# df = pd.read_csv(output_matix_intervals)
# print(df)
# df.plot.bar(x='Parameters', y=df.iloc[1:].columns)
# plt.xlabel('Parameters')
# plt.ylabel('Percentages')
# plt.show()