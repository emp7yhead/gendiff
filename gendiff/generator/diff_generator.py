import json

IN_FIRST = '- '
IN_SECOND = '+ '
BOTH = '  '


def generate_diff(file_path1, file_path2):
    first_file = json.load(open(file_path1))
    second_file = json.load(open(file_path2))
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

    return json.dumps(result, indent=2, sort_keys=True).replace('"', '')
