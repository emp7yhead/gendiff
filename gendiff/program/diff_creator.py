import json
import yaml

TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')
VALUE_DELETED = 'deleted'
VALUE_ADDED = 'added'
VALUE_CHANGED = 'changed'
VALUE_UNCHANGED = 'unchanged'
VALUE_CHILD = 'child'


def parce_data(file_path):
    if file_path.endswith(TYPE_JSON):
        data = json.load(open(file_path))

    if file_path.endswith(TYPE_YML_OR_YAML):
        data = yaml.safe_load(open(file_path))

    return data


def create_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []

    for key in sorted(keys):
        collected_data = {}

        if key not in data1:
            collected_data['status'] = VALUE_ADDED
            collected_data['key'] = key
            collected_data['value'] = data2[key]

        elif key not in data2:
            collected_data['status'] = VALUE_DELETED
            collected_data['key'] = key
            collected_data['value'] = data1[key]

        elif data1[key] == data2[key]:
            collected_data['status'] = VALUE_UNCHANGED
            collected_data['key'] = key
            collected_data['value'] = data1[key]

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            collected_data['status'] = VALUE_CHILD
            collected_data['key'] = key
            collected_data['child'] = create_diff(data1[key], data2[key])

        else:
            collected_data['status'] = VALUE_CHANGED
            collected_data['key'] = key
            collected_data['value1'] = data1[key]
            collected_data['value2'] = data2[key]

        result.append(collected_data)

    return result


def get_status(collected_data):
    return collected_data.get('status')


def get_key(collected_data):
    return collected_data.get('key')


def get_value(collected_data):
    value = collected_data.get('value', None)
    if value is None:
        value = (collected_data.get('value1'), collected_data.get('value2'))
    return value


def get_child(collected_data):
    return collected_data.get('child', None)
