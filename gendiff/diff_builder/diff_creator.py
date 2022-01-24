VALUE_DELETED = 'deleted'
VALUE_ADDED = 'added'
VALUE_CHANGED = 'changed'
VALUE_UNCHANGED = 'unchanged'
VALUE_CHILD = 'child'


def create_diff(data1, data2):
    keys = data1.keys() | data2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(collect_diff_segments(key, data1, data2))
    return diff


def collect_diff_segments(key, data1, data2):
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
    return collected_data


def create_diff_segment(type, key, value1, value2=None, child=None):
    collected_data = {
        'type': type,
        'key': key,
        'value_old': value1,
        'value_new': value2,
        'child': child
    }
    return collected_data


def get_type(collected_data):
    return collected_data.get('type')


def get_key(collected_data):
    return collected_data.get('key')


def get_value(collected_data):
    value = (collected_data.get('value_old'), collected_data.get('value_new'))
    return value


def get_child(collected_data):
    return collected_data.get('child', None)
