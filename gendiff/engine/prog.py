import argparse

from gendiff.program import diff_generator

DESCRIPTION = 'Generate diff'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = 'set format of output'


def parse_arguments():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(FORMAT_FLAG_1,
                        FORMAT_FLAG_2,
                        help=FORMAT_HELP,
                        default=diff_generator.FORMAT_STYLISH)
    args = parser.parse_args()
    print(diff_generator.generate_diff(args.first_file,
                                       args.second_file,
                                       args.format))
