import json
import yaml

TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')


def parce_data(file_path):
    if file_path.endswith(TYPE_JSON):
        parced_data = json.load(open(file_path))
    elif file_path.endswith(TYPE_YML_OR_YAML):
        parced_data = yaml.safe_load(open(file_path))
    else:
        raise NameError('Please choose valid file.')
    return parced_data
