from gendiff.program.diff_creator import parce_data, create_diff
from gendiff.program.stylish import build_result


def generate_diff(file_path1, file_path2):
    data1 = parce_data(file_path1)
    data2 = parce_data(file_path2)
    return build_result(create_diff(data1, data2))
