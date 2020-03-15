#!/usr/bin/env python3
import argparse
import sys
import statistics as stat


def parse_fasta(database: str) -> dict:
    # read from stdin if no filename provided
    if database == '-':
        # write to .temp file because Chem needs filename
        with open('.temp', 'w') as temp:
            temp.writelines([line for line in sys.stdin])
        database = '.temp'

    seqs_length = []
    seqs = []
    letters = {}
    with open(database) as db:
        prots_db = db.read()
        prots_db_splitted = prots_db.split('>')
        # omit first prot which is empty
        prots_db_splitted = prots_db_splitted[1:]
        for prot in prots_db_splitted:
            prot_lines = prot.splitlines()
            seq = ''.join(prot_lines[1:])
            for letter in seq:
                if letter in letters:
                    letters[letter] += 1
                else:
                    letters[letter] = 1
            # print(f'Len: {len(seq)}')
            seqs_length.append(len(seq))
            seqs.append(seq)

    stdev = stat.stdev(seqs_length)
    average = sum(seqs_length) / len(seqs_length)
    all_letters = sum([letter_cnt for letter_cnt in letters.values()])
    print(f'Average sequence length: {average:.2f}')
    print(f'Standard deviation: {stdev:.2f}')
    print(f'Sequences sum length: {all_letters}')
    print(f'Sequence letters frequencies:')
    for letter, letter_cnt in letters.items():
        print(f'\t{letter.upper()}: {float(letter_cnt) * 100 / float(all_letters):.2f}%')
    print('\n')

    return {'seqs': seqs, 'lengths': seqs_length, 'average': average, 'letters': letters, 'stdev': stdev}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('database', nargs='?', default='-', type=str,
                        help='database filename')
    args = parser.parse_args()
    parse_fasta(args.database)


if __name__ == '__main__':
    main()
