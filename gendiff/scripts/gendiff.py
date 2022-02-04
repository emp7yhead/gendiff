"""Main script of gendiff."""
from gendiff.cli import cli
from gendiff.diff_builder import diff_generator


def main() -> None:
    """Print diff between two files."""
    first_file, second_file, style_format = cli.parse_arguments()
    rendered_diff = diff_generator.generate_diff(
        first_file,
        second_file,
        style_format,
    )
    print(rendered_diff)  # noqa: WPS421


if __name__ == '__main__':
    main()
