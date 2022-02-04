"""Tests for extension."""
import pytest
from gendiff.diff_builder import data_loader

TEST_TEMPLATE = [
    (
        'tests/fixtures/nested1.json',
        '.json',
    ),
    (
        'tests/fixtures/nested1.yml',
        ('.yml', '.yaml'),
    ),
    pytest.param(
        'tests/fixtures/nested1.psd',
        '.psd',
        marks=pytest.mark.xfail,
    ),
]


@pytest.mark.parametrize('test_case, expected_result', TEST_TEMPLATE)
def test_get_file_extension(test_case, expected_result):
    """Test for coorect work with extensions.

    Args:
        test_case: file paths with different extensions.
        expected_result: expected output.
    """
    extension = data_loader.get_file_extension(test_case)
    assert extension == expected_result
