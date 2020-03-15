#!/usr/bin/env python3
import argparse
import numpy as np
import fasta
import matplotlib.pyplot as plt


def show_plt(lengths, organism, limit: int):
    plt.hist(lengths, 1000, facecolor='blue', alpha=0.5)
    plt.axvline(np.mean(lengths), color='green', linestyle='dashed', linewidth=1)
    plt.axvline(np.median(lengths), color='red', linestyle='dashed', linewidth=1)
    min_ylim, max_ylim = plt.ylim()
    plt.text(np.mean(lengths) * 1.1, max_ylim * 0.9, 'Mean: {:.0f}'.format(np.mean(lengths)))
    plt.text(np.median(lengths) * 1.1, max_ylim * 0.8, 'Median: {:.0f}'.format(np.median(lengths)))
    plt.ylabel('Proteins counts')
    plt.xlabel('Proteins lengths')
    axes = plt.gca()
    axes.set_xlim([0, limit])
    plt.title(f'{organism} proteins histogram')
    plt.savefig(f'{organism}-phist.png')
    plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('databases', nargs='+', type=str, help='databases')
    parser.add_argument('-l', '--limit', type=int, default=3000, help='protein lengths limit')
    args = parser.parse_args()

    out = {database: fasta.parse_fasta(database) for database in args.databases}

    for organism_name, info in out.items():
        organism_name = organism_name[:-len('.fasta')] if organism_name.endswith('.fasta') else organism_name
        show_plt(info['lengths'], organism_name, args.limit)


if __name__ == '__main__':
    main()
