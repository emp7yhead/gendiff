import json
import yaml

TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')

FILE_ERROR = 'Please choose valid file.'


def parse_data(file_path):
    file_extension = get_file_extension(file_path)
    if file_extension == TYPE_JSON:
        parsed_data = get_data_json(file_path)
    else:
        parsed_data = get_data_yml(file_path)
    return parsed_data


def get_file_extension(file_path):
    if file_path.endswith(TYPE_JSON):
        file_extension = TYPE_JSON
    elif file_path.endswith(TYPE_YML_OR_YAML):
        file_extension = TYPE_YML_OR_YAML
    else:
        raise NameError(FILE_ERROR)
    return file_extension


def get_data_json(file_path):
    data = json.load(open(file_path))
    return data


def get_data_yml(file_path):
    data = yaml.safe_load(open(file_path))
    return data
