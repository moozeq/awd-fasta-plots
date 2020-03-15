# Description
Creating plots for FASTA amino-acids files.

# Example usage

## Creating average protein length bar plot for Yeast, E. coli and Human:

```bash
./avg_length.py Yeast.fasta Ecoli.fasta Human.fasta
```

![alt text](https://github.com/moozeq/AWD_FASTA_plots/raw/master/plots/avg_length.png "Average protein sequence lengths")

## Creating average protein length histogram for Yeast:

```bash
./avg_length_hist.py Yeast.fasta
```

![alt text](https://github.com/moozeq/AWD_FASTA_plots/raw/master/plots/Yeast-phist.png "Protein sequence lengths histogram")

## Creating amino acids frequencies grouped bar plot for Yeast, E. coli and Human:

```bash
./aa_freqs.py Yeast.fasta Ecoli.fasta Human.fasta
```

![alt text](https://github.com/moozeq/AWD_FASTA_plots/raw/master/plots/aa_freqs.png "Amino acids frequencies multispecies comparision")