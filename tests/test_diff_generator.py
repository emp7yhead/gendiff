"""Tests for diff_generator.py."""
import pytest
from gendiff.diff_builder.diff_generator import generate_diff


@pytest.mark.parametrize(
    'file_path1, file_path2, test_format, correct_result', [
        (
            'tests/fixtures/nested1.yml',
            'tests/fixtures/nested2.yaml',
            'stylish',
            'tests/fixtures/results/format_stylish.txt',
        ),
        (
            'tests/fixtures/nested1.json',
            'tests/fixtures/nested2.json',
            'plain',
            'tests/fixtures/results/format_plain.txt',
        ),
        (
            'tests/fixtures/nested1.json',
            'tests/fixtures/nested2.json',
            'json',
            'tests/fixtures/results/format_json.txt',
        ),
        pytest.param(
            'tests/fixtures/nested1.json',
            'tests/fixtures/nested2.json',
            'strange',
            'tests/fixtures/results/format_json.txt',
            marks=pytest.mark.xfail,
        ),
    ],
)
def test_generate_diff(file_path1, file_path2, test_format, correct_result):
    """Test forcorrect structure of generated diff.

    Args:
        file_path1: path to first test file.
        file_path2: path to second test file.
        test_format: format for diff.
        correct_result: path to file with correct output diff.
    """
    with open(correct_result, 'r') as result_file:
        expected_result = result_file.read()
    test_diff = generate_diff(file_path1, file_path2, test_format)
    assert test_diff == expected_result
