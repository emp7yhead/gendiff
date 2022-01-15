from gendiff.program.data_parser import parse_data
from gendiff.program.diff_creator import create_diff
from gendiff.formatter.stylish import build_stylish
from gendiff.formatter.plain import build_plain
from gendiff.formatter.json import build_json

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

FORMAT_ERROR = 'Please choose valid format.'


def get_diff(file_path1, file_path2):
    data1 = parse_data(file_path1)
    data2 = parse_data(file_path2)
    diff = create_diff(data1, data2)
    return diff


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
    diff = get_diff(file_path1, file_path2)
    rendered_diff = render_diff(diff, style)
    return rendered_diff
