import pytest
from gendiff.diff_builder import data_loader


def test_get_file_data_json():
    test_case = 'tests/fixtures/nested_1.json'
    data, extension = data_loader.get_file_data(test_case)
    expected_data = open(test_case, 'r')
    assert data, extension == (expected_data, '.json')


def test_get_file_data_yaml():
    test_case = 'tests/fixtures/nested_1.yml'
    data, extension = data_loader.get_file_data(test_case)
    expected_data = open(test_case, 'r')
    assert data, extension == (expected_data, ('.yml', '.yaml'))


@pytest.mark.xfail
def test_get_file_data_fail():
    test_case = 'tests/fixtures/nested_1.psd'
    assert test_case
