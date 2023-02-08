import pandas as pd
import sys
import os

def main():
    f = sys.argv[1]
    if f.endswith('.tsv'):
        data = pd.read_csv(f, sep='\t', header=0, skiprows=None, usecols=("convertedBaseCount", "unconvertedBaseCount"))
        data.loc["sum"] = data.sum()
        convertedSum = data.loc['sum', 'convertedBaseCount']
        unconvertedSum = data.loc['sum', 'unconvertedBaseCount']
        perc_converted = round(convertedSum/unconvertedSum*100, 2)
        print(os.path.basename(f),'\n','Converted bases: ', convertedSum, '\n Unconverted bases: ', unconvertedSum, '\n Percent converted: ', perc_converted)

if __name__ == "__main__":
    main()