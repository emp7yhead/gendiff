import argparse

DESCRIPTION = 'Generate diff'
FIRST_FILE_VAR = 'first_file'
SECOND_FILE_VAR = 'second_file'

def parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(FIRST_FILE_VAR)
    parser.add_argument(SECOND_FILE_VAR)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(args.echo)
    