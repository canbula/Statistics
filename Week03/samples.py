import pandas as pd
import random


class Samples:
    def __init__(self, csv_file, delimiter=';'):
        self.csv_file = csv_file
        self.delimiter = delimiter
        self.df = pd.read_csv(self.csv_file, delimiter=self.delimiter)
    
    def simple_random_sample(self, sample_size, replace=False):
        return self.df.sample(sample_size, replace=replace)
    
    def stratified_sample(self, sample_size, masks, replace=False):
        df = pd.DataFrame()
        for mask in masks:
            df = pd.concat([df, self.df[mask].sample(int(sample_size/len(masks)), replace=replace)])
        return df
    
    def cluster_sample(self, sample_size, masks, replace=False):
        df = pd.DataFrame()
        if replace:
            selected_clusters = random.choices(masks, k=sample_size)
        else:
            selected_clusters = random.sample(masks, k=sample_size)
        for mask in selected_clusters:
            df = pd.concat([df, self.df[mask]])
        return df
    
    def systematic_sample(self, sample_size):
        return self.df.iloc[::int(len(self.df)/sample_size)]


def main():
    samples = Samples('Week02/turkey_earthquakes.csv', delimiter=';')
    # Simple Random Sample
    print(samples.simple_random_sample(100).info)
    print(samples.simple_random_sample(100, replace=True).info) # True Random Sampling
    # Stratified Sample
    masks = [
        samples.df['Yer'].str.contains('ISTANBUL'),
        samples.df['Yer'].str.contains('ANKARA'),
        samples.df['Yer'].str.contains('IZMIR'),
        ~samples.df['Yer'].str.contains('ISTANBUL|ANKARA|IZMIR'),
    ]
    print(samples.stratified_sample(20, masks, replace=True).info)
    # Cluster Random Sample
    masks = [
        samples.df['Olus tarihi'].str[:4].astype(int) >= 2000,
        samples.df['Olus tarihi'].str.split('.').str[0].astype(int) < 2000,
        samples.df['Derinlik'].astype(float) > 10,
        samples.df['xM'].astype(float) > 5, 
    ]
    print(samples.cluster_sample(2, masks).info)
    # Systematic Sample
    print(samples.systematic_sample(250).info)


if __name__ == "__main__":
    main()
