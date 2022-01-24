from gendiff.diff_builder import diff_creator

TEMPLATE_ADDED = "Property '{path}' was added with value: {value}"
TEMPLATE_DELETED = "Property '{path}' was removed"
TEMPLATE_CHANGED = "Property '{path}' was updated. From {value1} to {value2}"

TEMPLATE_COMPLEX_VALUE = '[complex value]'


def build_plain(tree, path=[]):
    data = []
    for node in tree:

        type = diff_creator.get_type(node)
        key = diff_creator.get_key(node)
        value = diff_creator.get_value(node)
        child = diff_creator.get_child(node)
        path.append(key)

        if type == diff_creator.VALUE_DELETED:
            data.append(build_string(TEMPLATE_DELETED, path, value[0]))
        elif type == diff_creator.VALUE_ADDED:
            data.append(build_string(TEMPLATE_ADDED, path, value[0]))
        elif type == diff_creator.VALUE_CHILD:
            data.append(build_plain(child, path))
        elif type == diff_creator.VALUE_CHANGED:
            data.append(build_string(TEMPLATE_CHANGED, path, value[0],
                                     value[1]))
        path.pop()
    return '\n'.join(data)


def build_string(template, path, value1, value2=None):
    if template != TEMPLATE_CHANGED:
        return template.format(path='.'.join(path), value=build_value(value1))
    else:
        return template.format(path='.'.join(path), value1=build_value(value1),
                               value2=build_value(value2))


def build_value(value):
    if isinstance(value, dict):
        value = TEMPLATE_COMPLEX_VALUE
    elif isinstance(value, bool):
        value = str(value).lower()
    elif isinstance(value, str):
        value = "'{}'".format(value)
    elif value is None:
        value = 'null'
    return value
