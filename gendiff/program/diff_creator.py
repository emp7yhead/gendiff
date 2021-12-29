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


def create_diff_segment(status, key, value1, value2=None, child=None):
    collected_data = {
        'status': status,
        'key': key,
        'value1': value1,
        'value2': value2,
        'child': child
    }
    return collected_data


def create_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):

        if key not in data1:
            collected_data = create_diff_segment(VALUE_ADDED,
                                                 key,
                                                 data2[key])
        elif key not in data2:
            collected_data = create_diff_segment(VALUE_DELETED,
                                                 key,
                                                 data1[key])
        elif data1[key] == data2[key]:
            collected_data = create_diff_segment(VALUE_UNCHANGED,
                                                 key,
                                                 data1[key])
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            collected_data = create_diff_segment(VALUE_CHILD,
                                                 key,
                                                 value1=None,
                                                 child=create_diff(data1[key],
                                                                   data2[key]))
        else:
            collected_data = create_diff_segment(VALUE_CHANGED,
                                                 key,
                                                 value1=data1[key],
                                                 value2=data2[key])
        result.append(collected_data)

    return result


def get_status(collected_data):
    return collected_data.get('status')


def get_key(collected_data):
    return collected_data.get('key')


def get_value(collected_data):
    value = (collected_data.get('value1'), collected_data.get('value2'))
    return value


def get_child(collected_data):
    return collected_data.get('child', None)
