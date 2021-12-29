from gendiff.program.diff_generator import generate_diff

plain_json1 = 'tests/fixtures/plain_1.json'
plain_json2 = 'tests/fixtures/plain_2.json'
plain_yml3 = 'tests/fixtures/plain_1.yaml'
plain_yml4 = 'tests/fixtures/plain_2.yml'

nested_json1 = 'tests/fixtures/nested_1.json'
nested_json2 = 'tests/fixtures/nested_2.json'
nested_yml1 = 'tests/fixtures/nested_1.yml'
nested_yml2 = 'tests/fixtures/nested_2.yaml'

expected_plain_result = 'tests/fixtures/plain_result.txt'
expected_nested_result = 'tests/fixtures/nested_result.txt'

plain_diff_json = generate_diff(plain_json1, plain_json2)
plain_diff_yml = generate_diff(plain_yml3, plain_yml4)
nested_diff_json = generate_diff(nested_json1, nested_json2)
nested_diff_yml = generate_diff(nested_yml1, nested_yml2)


def test_generate_diff():
    assert plain_diff_json == open(expected_plain_result, 'r').read()
    assert plain_diff_yml == open(expected_plain_result, 'r').read()
    assert nested_diff_json == open(expected_nested_result, 'r').read()
    assert nested_diff_yml == open(expected_nested_result, 'r').read()
