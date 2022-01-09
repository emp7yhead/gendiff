import pytest
from gendiff.program.diff_generator import generate_diff


def test_generate_diff_plain():
    expected_plain_result = 'tests/fixtures/plain_result.txt'

    plain_yml3 = 'tests/fixtures/plain_1.yaml'
    plain_yml4 = 'tests/fixtures/plain_2.yml'

    plain_diff = generate_diff(plain_yml3, plain_yml4)

    assert plain_diff == open(expected_plain_result, 'r').read()


def test_generate_diff_nested():
    expected_nested_result = 'tests/fixtures/nested_result.txt'

    nested_json1 = 'tests/fixtures/nested_1.json'
    nested_json2 = 'tests/fixtures/nested_2.json'

    nested_diff = generate_diff(nested_json1, nested_json2)

    assert nested_diff == open(expected_nested_result, 'r').read()


def test_generate_diff_format_plain():
    expected_format_plain_result = 'tests/fixtures/format_plain_result.txt'

    nested_json1 = 'tests/fixtures/nested_1.json'
    nested_json2 = 'tests/fixtures/nested_2.json'

    format_plain_diff = generate_diff(nested_json1, nested_json2, 'plain')

    assert format_plain_diff == open(expected_format_plain_result, 'r').read()


@pytest.mark.xfail(raises=NameError)
def test_generate_diff_format_error():
    nested_json1 = 'tests/fixtures/nested_1.json'
    nested_json2 = 'tests/fixtures/nested_2.json'

    generate_diff(nested_json1, nested_json2, 'changed')
