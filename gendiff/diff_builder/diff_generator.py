from gendiff.diff_builder.data_loader import get_file_data
from gendiff.diff_builder.data_parser import parse_data
from gendiff.diff_builder.diff_creator import create_diff
from gendiff.formatter.stylish import build_stylish
from gendiff.formatter.plain import build_plain
from gendiff.formatter.json import build_json

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

FORMAT_ERROR = 'Please choose valid format.'


def render_diff(diff, style):
    if style == FORMAT_STYLISH:
        return build_stylish(diff)
    elif style == FORMAT_PLAIN:
        return build_plain(diff)
    elif style == FORMAT_JSON:
        return build_json(diff)
    else:
        raise NameError(FORMAT_ERROR)


def generate_diff(file_path1, file_path2, style=FORMAT_STYLISH):
    data1, extension1 = get_file_data(file_path1)
    data2, extension2 = get_file_data(file_path2)

    parsed_data1 = parse_data(data1, extension1)
    parsed_data2 = parse_data(data2, extension2)

    diff = create_diff(parsed_data1, parsed_data2)
    return render_diff(diff, style)
