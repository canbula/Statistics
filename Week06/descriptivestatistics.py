import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DescriptiveStatistics:
    def __init__(self, data):
        self.data = data
    
    def frequency_table(self):
        possible_values = sorted(set(self.data))
        counters = {x: 0 for x in possible_values}
        for x in counters:
            counters[x] = self.data.count(x)
        cumulative_relative_frequency = 0.0
        table_lines = []
        for k, v in counters.items():
            cumulative_relative_frequency += v/len(self.data)
            table_lines.append([
                k, v, v/len(self.data), cumulative_relative_frequency
            ])
        return pd.DataFrame(
            table_lines, 
            columns=["Value", "Frequency", "Relative Freq.", "Cumulative Rel. Freq."]
            )
    
    def data_matrix(self):
        for i, x in enumerate(sorted(self.data)):
            print(f"{x:4d}", end="")
            if (i+1)%10 == 0:
                print("")
    
    def stem_and_leaf_plot(self, stems):
        for s in stems:
            v = [str(n-s[0]) for n in sorted(self.data) if n>=s[0] and n<=s[1]]
            v_str = " ".join(v)
            print(f"{s[0]//10} | {v_str}")
    
    def boxplot(self):
        return pd.Series(self.data).plot.box()


def main():
    random.seed(210316017)
    print("# Frequency Table #")
    data = [random.randint(1, 9) for _ in range(100)]
    descriptive_statistics = DescriptiveStatistics(data)
    print(descriptive_statistics.frequency_table())
    del data, descriptive_statistics
    print("")
    print("# Data Matrix #")
    data = [random.randint(10, 99) for _ in range(100)]
    descriptive_statistics = DescriptiveStatistics(data)
    descriptive_statistics.data_matrix()
    print("")
    print("# Stem-and-Leaf Plot")
    stems = [
        (10, 19),
        (20, 29),
        (30, 39),
        (40, 49),
        (50, 59),
        (60, 69),
        (70, 79),
        (80, 89),
        (90, 99)
    ]
    descriptive_statistics.stem_and_leaf_plot(stems)
    descriptive_statistics.data.pop()
    descriptive_statistics.data.append(180)
    plt.figure()
    descriptive_statistics.boxplot()
    plt.show()


if __name__ == "__main__":
    main()
