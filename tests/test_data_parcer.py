import json
import yaml
import pytest
from gendiff.diff_builder import data_parser


@pytest.mark.parametrize(
    'file_name, expected',
    [
        ('python.json', '.json'),
        ('python.yml', ('.yml', '.yaml')),
        pytest.param(
            'strange.psd', '.psd', marks=pytest.mark.xfail
            )
    ]
)
def test_get_data_extension(file_name, expected):
    extension = data_parser.get_file_extension(file_name)
    assert extension == expected


def test_parse_data():
    test_case1 = 'tests/fixtures/nested_1.json'
    test_case2 = 'tests/fixtures/nested_1.yml'
    result1 = json.load(open(test_case1))
    result2 = yaml.safe_load(open(test_case2))
    assert data_parser.parse_data(test_case1) == result1
    assert data_parser.parse_data(test_case2) == result2
