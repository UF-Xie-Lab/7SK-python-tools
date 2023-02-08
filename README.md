# 7SK-python-tools
A set of scripts in python used for analysis of ChIP-seq and SLAM-seq datasets

conversion_rate.py takes in a conversion table, as output by `hisat-3n-table` from HISAT-3N, and determines the total percent of converted bases relative to the total number of bases.

traveling_ratio.py takes in a gzipped matrix file, as output by deepTools' `computeMatrix scale-regions` from RNA polymerase II ChIP-seq data and calculates the traveling ratio. The traveling ratio is defined as the ratio of reads from 300 bp downstream of the TSS to 3kb downstream of the TES over the reads from 30 bp upstream of the TSS to 300 bp downstream of the TSS.
