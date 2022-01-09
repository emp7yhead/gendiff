from gendiff.program.diff_creator import parce_data, create_diff
from gendiff.formatter.stylish import build_stylish
from gendiff.formatter.plain import build_plain

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'

ERROR = 'Please choose valid format.'


def generate_diff(file_path1, file_path2, style=FORMAT_STYLISH):
    data1 = parce_data(file_path1)
    data2 = parce_data(file_path2)
    if style == FORMAT_STYLISH:
        return build_stylish(create_diff(data1, data2))
    elif style == FORMAT_PLAIN:
        return build_plain(create_diff(data1, data2))
    else:
        raise NameError(ERROR)
