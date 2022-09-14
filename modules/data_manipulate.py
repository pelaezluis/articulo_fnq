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

    ############################# ONLY DISTANCES ####################################

    def extract_distances(self, output_file: str = ''):
        """
            Extract only the distances for all fnqs
        """
        df = self.load()
        df_ = df[['FNQ', 'Mode', 'c3a', 'c4a', 'c8a', 'c9a']]
        if output_file != '':
            print(f'Saving {output_file}...')
            df_.to_csv(output_file, index=False)
        return df_


    def extract_distances_by_fnq(self, fnq: str, output_file: str = ''):
        """
            Extract only the distances for all fnqs
        """
        df = self.extract_distances()
        df_ = df.loc[df['FNQ'] == fnq]
        if output_file != '':
            print(f'Saving {output_file}...')
            df_.to_csv(output_file, index=False)
        return df_

    
    def extract_distances_by_fnq_and_mode(self, fnq: str, mode: str, output_file: str = ''):
        """
            Extract only the distances for all fnqs
        """
        df = self.extract_distances_by_fnq(fnq=fnq)
        df_ = df.loc[df['Mode'] == mode]
        if output_file != '':
            print(f'Saving {output_file}...')
            df_.to_csv(output_file, index=False)
        return df_


    def verify_intervals(self, distance_list: list, min: float, max: float, condition: int = 1):
        counter: int = 0
        for distance in distance_list:
            if min <= distance <= max:
                counter += 1
        if counter >= condition:
            return counter


    def count_distances_in_interval(self, min: float, max: float, condition: int = 1):
        """
            Calculate percentage of data in interval for all the fnq
        """
        df = self.extract_distances()
        df_ = df.iloc[:, 2:].apply(self.verify_intervals, args=(min, max, condition), axis=1)
        return round((df_.count() * 100 ) / len(df_), 3)

    
    def distances_in_interval_by_fnq(self, fnq: str, min: float, max: float, condition: int):
        """
            Calculate percentage of data in interval for an specific fnq
        """
        df = self.extract_distances_by_fnq(fnq=fnq)
        df_ = df.iloc[:, 2:].apply(self.verify_intervals, args=(min, max, condition), axis=1)             
        return round((df_.count() * 100 ) / len(df_), 3)


    def fnq_list(self) -> list:
        df = self.extract_distances()
        fnqs = df['FNQ'].unique()
        return sorted(fnqs)


    def matrix_interval_distance(self, min: float, max: float, output_file: str = ''):
        fnqs = self.fnq_list()
        params = ['1', '2', '3', '4']
        df = {'Parameters': params}
        print('#'*53)
        for fnq in fnqs:
            percentages_per_fnq = []
            for cont in range(1, 5):
                percentage = self.distances_in_interval_by_fnq(fnq, min, max, cont)
                print(f'# Para {fnq} con {cont} parametros el porcentaje es: {percentage} ')
                percentages_per_fnq.append(percentage)
            df[fnq] = percentages_per_fnq
            print('#'*53)
        df = pd.DataFrame(df)
        if output_file != '':
            df.to_csv(output_file, index=False)
            return df
        else:
            return df
                
    ############################# ENERGIES AND DISTANCES ####################################


    def extract_energies_distances_by_fnq(self, fnq: str):
        """
            Extract all the energies and distances for a given fnq
        """
        df = self.load()
        return df.loc[df['FNQ'] == fnq]
    

    def extract_energies_distances_by_fnq_and_mode(self, fnq: str, mode: str):
        """
            Extract all the energies and distances for the fnq and mode given
        """
        df = self.load()
        return df.loc[(df['FNQ'] == fnq) & (df['Mode'] == mode)]

    
    def extract_energy_distances_by_residue(self, residue: str, output_file: str = ''):
        """
            Extract a residue energy for all the fnqs
        """
        df = self.load()
        df_ = df[['FNQ', 'Mode', residue, 'c3a', 'c4a', 'c8a', 'c9a']]
        if output_file != '':
            print(f'Saving {output_file}...')
            df_.to_csv(output_file, index=False)
        return df_

    
    def extract_energy_distances_by_residue_and_fnq(self, residue: str, fnq: str, output_file: str = ''):
        """
            Extract energy only for a residue and fnq
        """
        df = self.extract_energies_distances_by_fnq(fnq)
        df_ = df[['FNQ', 'Mode', residue, 'c3a', 'c4a', 'c8a', 'c9a']]
        if output_file != '':
            print(f'Saving {output_file}...')
            df_.to_csv(output_file, index=False)
        return df_