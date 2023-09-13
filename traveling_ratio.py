import pandas as pd
import sys

def main():
    f = sys.argv[1]
    if f.endswith(".gz"):
        data = pd.read_csv(f, compression='gzip' , sep='\t', header=None, skiprows=1)
        data = data.drop(axis=1, labels=[0, 1, 2, 3, 4, 5])
        data.loc['total'] = data.sum(axis=0)
        TSS_IP1 = (data.loc['total', 104:206]).sum()
        TSS_IP2 = (data.loc['total', 2604:2706]).sum()
        TSS_IP3 = (data.loc['total', 5104:5206]).sum()
        GB_IP1 = (data.loc['total', 207:2506]).sum()
        GB_IP2 = (data.loc['total', 2707:5006]).sum()
        GB_IP3 = (data.loc['total', 5207:7506]).sum()
        TR_IP1 = GB_IP1/TSS_IP1
        TR_IP2 = GB_IP2/TSS_IP2
        TR_IP3 = GB_IP3/TSS_IP3
        print("IP1 Traveling Ratio: ", TR_IP1, "IP2 Traveling Ratio: ", TR_IP2, "IP3 Traveling Ratio: ", TR_IP3)

if __name__ == "__main__":
    main()
