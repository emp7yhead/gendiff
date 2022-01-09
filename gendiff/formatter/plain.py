from gendiff.program import diff_creator

TEMPLATE_ADDED = "Property '{path}' was added with value: {value}"
TEMPLATE_DELETED = "Property '{path}' was removed"
TEMPLATE_CHANGED = "Property '{path}' was updated. From {value1} to {value2}"

TEMPLATE_COMPLEX_VALUE = '[complex value]'


def build_plain(tree, path=[]):
    final_result = []
    for node in tree:

        status = diff_creator.get_status(node)
        key = diff_creator.get_key(node)
        value = diff_creator.get_value(node)
        child = diff_creator.get_child(node)
        path.append(key)

        if status == diff_creator.VALUE_DELETED:
            final_result.append(build_string(TEMPLATE_DELETED, path, value[0]))
        elif status == diff_creator.VALUE_ADDED:
            final_result.append(build_string(TEMPLATE_ADDED, path, value[0]))
        elif status == diff_creator.VALUE_CHILD:
            final_result.append(build_plain(child, path))
        elif status == diff_creator.VALUE_CHANGED:
            final_result.append(build_string(TEMPLATE_CHANGED, path, value[0],
                                             value[1]))
        path.pop()
    return '\n'.join(final_result)


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
