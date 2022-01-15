from gendiff.cli import cli
from gendiff.diff_builder import diff_generator


def main():
    first_file, second_file, format = cli.parse_arguments()
    rendered_diff = diff_generator.generate_diff(first_file,
                                                 second_file,
                                                 format)
    print(rendered_diff)


if __name__ == '__main__':
    main()
