"""Function to generate diff between two files."""

from gendiff.diff_builder.data_loader import get_file_data_and_extension
from gendiff.diff_builder.data_parser import parse_data
from gendiff.diff_builder.diff_creator import create_diff
from gendiff.formatter.renderer import FORMAT_STYLISH, render_diff


def generate_diff(  # noqa: WPS210
    file_path1: str,
    file_path2: str,
    style: str = FORMAT_STYLISH,
) -> str:  # noqa: WPS210
    """Generate diff between two files using chosen style.

    Args:
        file_path1: absolute or relative path to first file.
        file_path2: absolute or relative path to second file.
        style: format of diff(stylish, plain or json, default: stylish)

    Returns:
        str
    """
    data1, extension1 = get_file_data_and_extension(file_path1)
    data2, extension2 = get_file_data_and_extension(file_path2)

    parsed_data1 = parse_data(data1, extension1)
    parsed_data2 = parse_data(data2, extension2)

    diff = create_diff(parsed_data1, parsed_data2)
    return render_diff(diff, style)
