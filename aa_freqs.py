#!/usr/bin/env python3
import argparse
import fasta
import matplotlib.pyplot as plt


# https://stackoverflow.com/a/60270421
def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True):
    """Draws a bar plot with multiple bars per data point.

    Parameters
    ----------
    ax : matplotlib.pyplot.axis
        The axis we want to draw our plot on.

    data: dictionary
        A dictionary containing the data we want to plot. Keys are the names of the
        data, the items is a list of the values.

        Example:
        data = {
            "x":[1,2,3],
            "y":[1,2,3],
            "z":[1,2,3],
        }

    colors : array-like, optional
        A list of colors which are used for the bars. If None, the colors
        will be the standard matplotlib color cyle. (default: None)

    total_width : float, optional, default: 0.8
        The width of a bar group. 0.8 means that 80% of the x-axis is covered
        by bars and 20% will be spaces between the bars.

    single_width: float, optional, default: 1
        The relative width of a single bar within a group. 1 means the bars
        will touch eachother within a group, values less than 1 will make
        these bars thinner.

    legend: bool, optional, default: True
        If this is set to true, a legend will be added to the axis.
    """

    # Check if colors where provided, otherwhise use the default color cycle
    if colors is None:
        colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

    # Number of bars per group
    n_bars = len(data)

    # The width of a single bar
    bar_width = total_width / n_bars

    # List containing handles for the drawn bars, used for the legend
    bars = []

    # Iterate over all data
    for i, (name, values) in enumerate(data.items()):
        # The offset in x direction of that bar
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        # Draw a bar for every value of that type
        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)])

        # Add a handle to the last drawn bar, which we'll need for the legend
        bars.append(bar[0])

    # Draw legend if we need
    if legend:
        ax.legend(bars, data.keys())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('databases', nargs='+', type=str, help='databases')
    args = parser.parse_args()

    out = {database: fasta.parse_fasta(database) for database in args.databases}

    organisms = [organism_name[:-len('.fasta')] if organism_name.endswith('.fasta') else organism_name for organism_name
                 in out.keys()]

    frequencies = [
        {letter: letter_cnt / sum([letter_cnt for letter_cnt in info['letters'].values()]) for letter, letter_cnt in
         info['letters'].items()}
        for info in out.values()
    ]

    # get all letters
    all_letters = {}
    for org_letters in frequencies:
        all_letters.update(org_letters)

    # sort by first organism
    keys = [k for k, v in sorted(frequencies[0].items(), key=lambda item: item[1])]

    # handle other letters if exist in other organisms
    keys_diff = [k for k in all_letters if k not in keys]
    keys = keys_diff + keys

    # prepare data
    data = {organisms[i]: [frequencies[i].get(letter, 0) for letter in keys] for i in range(0, len(organisms))}

    fig, ax = plt.subplots()
    bar_plot(ax, data, total_width=.8, single_width=.9)
    plt.xticks(range(len(keys)), list(keys))

    plt.title(f'Amino acids frequencies for selected organisms')
    plt.ylabel('Amino acids frequency [%]')
    plt.xlabel('Amino acids')
    plt.savefig(f'aa_freqs.png')
    plt.show()
