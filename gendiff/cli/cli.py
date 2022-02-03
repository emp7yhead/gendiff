"""Function to parse arguments in CLI."""
import argparse

from gendiff.diff_builder import diff_generator

DESCRIPTION = 'Generate diff'
FORMAT_FLAG1 = '-f'
FORMAT_FLAG2 = '--format'
FORMAT_HELP = 'set format of output'


def parse_arguments():
    """
    Parse arguments for gendiff.

    Returns:
        args.first_file: str
        args.second_file: str
        args.format: str
    """
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        FORMAT_FLAG1,
        FORMAT_FLAG2,
        help=FORMAT_HELP,
        default=diff_generator.FORMAT_STYLISH,
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format
