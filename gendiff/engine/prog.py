import argparse

DESCRIPTION = 'Generate diff'
FIRST_FILE_VAR = 'first_file'
SECOND_FILE_VAR = 'second_file'
FORMAT_FLAG_1 = '-f'
FORMAT_FLAG_2 = '--format'
FORMAT_HELP = 'set format of output'


def parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(FIRST_FILE_VAR)
    parser.add_argument(SECOND_FILE_VAR)
    parser.add_argument(FORMAT_FLAG_1, FORMAT_FLAG_2, help=FORMAT_HELP)
    args = parser.parse_args()
    print(args.echo)
