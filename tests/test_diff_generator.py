import pytest
from gendiff.diff_builder.diff_generator import generate_diff


@pytest.mark.parametrize(
    'file_path1, file_path2, test_format, result', [
        ('tests/fixtures/nested_1.yml',
         'tests/fixtures/nested_2.yaml',
         'stylish',
         'tests/fixtures/results/format_stylish.txt'),
        ('tests/fixtures/nested_1.json',
         'tests/fixtures/nested_2.json',
         'plain',
         'tests/fixtures/results/format_plain.txt'),
        ('tests/fixtures/nested_1.json',
         'tests/fixtures/nested_2.json',
         'json',
         'tests/fixtures/results/format_json.txt'),
        pytest.param('tests/fixtures/nested_1.json',
                     'tests/fixtures/nested_2.json',
                     'strange',
                     'tests/fixtures/results/format_json.txt',
                     marks=pytest.mark.xfail),
    ]
)
def test_generate_diff(file_path1, file_path2, test_format, result):
    expected_result = open(result, 'r').read()
    test_diff = generate_diff(file_path1, file_path2, test_format)
    assert test_diff == expected_result
