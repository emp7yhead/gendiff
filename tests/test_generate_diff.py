import json
from gendiff.program.diff_generator import generate_diff

file_path1 = 'tests/fixtures/file1.json'
file_path2 = 'tests/fixtures/file2.json'
file_path3 = 'tests/fixtures/file1.yaml'
file_path4 = 'tests/fixtures/file2.yml'
diff1 = generate_diff(file_path1, file_path2)
diff2 = generate_diff(file_path3, file_path4)
expexted_result = '{\n  - follow: false,\n    host: hexlet.io,\n  - proxy: 123.234.53.22,\n  - timeout: 50,\n  + timeout: 50,\n  + verbose: true\n}'

def test_diff():
    assert diff1 == expexted_result
    assert diff2 == expexted_result