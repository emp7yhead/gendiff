from gendiff.diff_builder.data_loader import get_file_data_and_extension
from gendiff.diff_builder.data_parser import parse_data
from gendiff.diff_builder.diff_creator import create_diff
from gendiff.formatter.renderer import render_diff, FORMAT_STYLISH


def generate_diff(file_path1, file_path2, style=FORMAT_STYLISH):
    data1, extension1 = get_file_data_and_extension(file_path1)
    data2, extension2 = get_file_data_and_extension(file_path2)

    parsed_data1 = parse_data(data1, extension1)
    parsed_data2 = parse_data(data2, extension2)

    diff = create_diff(parsed_data1, parsed_data2)
    return render_diff(diff, style)
