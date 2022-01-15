import argparse

from gendiff.diff_builder import diff_generator

DESCRIPTION = 'Generate diff'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = 'set format of output'


def parse_arguments():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(FORMAT_FLAG_1,
                        FORMAT_FLAG_2,
                        help=FORMAT_HELP,
                        default=diff_generator.FORMAT_STYLISH)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
