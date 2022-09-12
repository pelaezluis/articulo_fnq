from os.path import isfile
import pandas as pd

class EnergyAndDistances:

    def __init__(self, input_file: str) -> None:
        self.input_file = input_file
        
    
    def load(self):
        if isfile(self.input_file):
            return pd.read_csv(self.input_file)
        else:
            return 'File does not exist'


    def show_data(self):
        print(self.load())


    def extract_energies_distances_by_fnq(self, fnq: str):
        df = self.load()
        return df.loc[df['FNQ'] == fnq]
    

    def extract_energies_distances_by_fnq_and_mode(self, fnq: str, mode: str):
        df = self.load()
        return df.loc[(df['FNQ'] == fnq) & (df['Mode'] == mode)]

    
    def extract_energy_distances_by_residue(self, residue: str):
        df = self.load()
        return df[['FNQ', 'Mode', residue, 'c3a', 'c4a', 'c8a', 'c9a']]

    
    def extract_energy_distances_by_residue_and_fnq(self, residue: str, fnq: str):
        df = self.extract_energies_distances_by_fnq(fnq)
        return df[['FNQ', 'Mode', residue, 'c3a', 'c4a', 'c8a', 'c9a']]