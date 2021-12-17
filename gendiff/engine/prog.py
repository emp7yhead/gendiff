import argparse

DESCRIPTION = 'Generate diff'


def parser():
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('First file', metavar='first_file')
    parser.add_argument('Second file', metavar='second_file')
    args = parser.parse_args()
    print(args.accumulate(args.integers))