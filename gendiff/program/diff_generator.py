import json
import yaml

IN_FIRST = '- '
IN_SECOND = '+ '
BOTH = '  '


def check_file_extension(file_path):
    if file_path.endswith('.json'):
        file = json.load(open(file_path))
    if file_path.endswith(('.yml', '.yaml')):
        file = yaml.safe_load(open(file_path))
    return file


def generate_diff(file_path1, file_path2):
    first_file = check_file_extension(file_path1)
    second_file = check_file_extension(file_path2)
    # create set of keys in files
    keys = first_file.keys() | second_file.keys()
    result = {}

    for key in keys:
        if key not in first_file:
            result[IN_SECOND + key] = second_file[key]
        elif key not in second_file:
            result[IN_FIRST + key] = first_file[key]
        elif first_file[key] == second_file[key]:
            result[BOTH + key] = first_file[key]
        else:
            result[IN_FIRST + key] = first_file[key]
            result[IN_SECOND + key] = first_file[key]

    # sorting result by first letter in key
    result_sorted = {key: result[key] for key in sorted(result,
                                                        key=lambda x: x[2])}
    return json.dumps(result_sorted, indent=2, sort_keys=False).replace('"', '')
