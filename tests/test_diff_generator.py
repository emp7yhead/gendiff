from gendiff.program.diff_generator import generate_diff

plain_yml3 = 'tests/fixtures/plain_1.yaml'
plain_yml4 = 'tests/fixtures/plain_2.yml'

nested_json1 = 'tests/fixtures/nested_1.json'
nested_json2 = 'tests/fixtures/nested_2.json'

expected_plain_result = 'tests/fixtures/plain_result.txt'
expected_nested_result = 'tests/fixtures/nested_result.txt'
expected_format_plain_result = 'tests/fixtures/format_plain_result.txt'

plain_diff = generate_diff(plain_yml3, plain_yml4)
nested_diff = generate_diff(nested_json1, nested_json2)
format_plain_diff = generate_diff(nested_json1, nested_json2, 'plain')


def test_generate_diff():
    assert plain_diff == open(expected_plain_result, 'r').read()
    assert nested_diff == open(expected_nested_result, 'r').read()
    assert format_plain_diff == open(expected_format_plain_result, 'r').read()
