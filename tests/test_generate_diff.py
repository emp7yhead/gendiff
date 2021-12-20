import json
from gendiff.program.diff_generator import generate_diff

diff = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
expexted_result = '{\n  - follow: false,\n    host: hexlet.io,\n  - proxy: 123.234.53.22,\n  - timeout: 50,\n  + timeout: 50,\n  + verbose: true\n}'

def test_diff():
    assert diff == expexted_result
