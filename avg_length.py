#!/usr/bin/env python3
import argparse
import numpy as np
import fasta
import matplotlib.pyplot as plt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('databases', nargs='+', type=str, help='databases')
    args = parser.parse_args()

    out = {database: fasta.parse_fasta(database) for database in args.databases}

    organisms = [organism_name for organism_name in out.keys()]
    averages = [info['average'] for info in out.values()]
    stdevs = [[info['stdev'] / 2 for info in out.values()]]

    # Make a dataset:
    height = averages
    bars = organisms
    y_pos = np.arange(len(bars))

    # Create bars
    plt.bar(y_pos, height)

    # Create names on the x-axis
    plt.xticks(y_pos, bars, rotation=45)

    # Add label on y-axis
    plt.ylabel('Average protein sequence length')

    # Create error bars based on standard deviation
    plt.errorbar(organisms, averages, yerr=stdevs, linestyle='None', ecolor='red')

    # Show graphic
    plt.show()


if __name__ == '__main__':
    main()
