import pytest
from gendiff.diff_builder import data_loader

TEST_TEMPLATE = [
    ('tests/fixtures/nested_1.json', '.json'),
    ('tests/fixtures/nested_1.yml', ('.yml', '.yaml')),
    pytest.param('tests/fixtures/nested_1.psd',
                 '.psd',
                 marks=pytest.mark.xfail)
    ]


@pytest.mark.parametrize('test_case, expected_result', TEST_TEMPLATE)
def test_get_file_extension(test_case, expected_result):
    extension = data_loader.get_file_extension(test_case)
    assert extension == expected_result
