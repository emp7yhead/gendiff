import argparse

from gendiff.program.diff_generator import generate_diff


DESCRIPTION = 'Generate diff'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = 'set format of output'


def parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(FORMAT_FLAG_1, FORMAT_FLAG_2, help=FORMAT_HELP)
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
