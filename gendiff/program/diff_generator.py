from gendiff.program.data_parcer import parce_data
from gendiff.program.diff_creator import create_diff
from gendiff.formatter.stylish import build_stylish
from gendiff.formatter.plain import build_plain
from gendiff.formatter.json import build_json

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

ERROR = 'Please choose valid format.'


def generate_diff(file_path1, file_path2, style=FORMAT_STYLISH):
    data1 = parce_data(file_path1)
    data2 = parce_data(file_path2)
    if style == FORMAT_STYLISH:
        return build_stylish(create_diff(data1, data2))
    elif style == FORMAT_PLAIN:
        return build_plain(create_diff(data1, data2))
    elif style == FORMAT_JSON:
        return build_json(create_diff(data1, data2))
    else:
        raise NameError(ERROR)
