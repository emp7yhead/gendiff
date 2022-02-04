"""Functions to build plain format for diff."""  # noqa: WPS232
from typing import Any, List

from gendiff.diff_builder import diff_creator

TEMPLATE_ADDED = "Property '{path}' was added with value: {value}"
TEMPLATE_DELETED = "Property '{path}' was removed"
TEMPLATE_CHANGED = "Property '{path}' was updated. From {value1} to {value2}"

TEMPLATE_COMPLEX_VALUE = '[complex value]'


def build_plain(  # noqa: WPS210, WPS231
    diff: Any,
    path: List = [],  # noqa: WPS404, B006
) -> str:
    """
    Build plain diff.

    Args:
        diff: diff tree between two files.
        path: path to value.

    Returns:
        str.
    """
    collected_data = []
    for node in diff:

        diff_type = diff_creator.get_diff_type(node)
        key = diff_creator.get_key(node)
        diff_value = diff_creator.get_value(node)
        child = diff_creator.get_child(node)
        path.append(key)

        if diff_type == diff_creator.VALUE_DELETED:
            collected_data.append(
                build_string(
                    TEMPLATE_DELETED,
                    path,
                    diff_value[0],
                ),
            )
        elif diff_type == diff_creator.VALUE_ADDED:
            collected_data.append(
                build_string(
                    TEMPLATE_ADDED,
                    path,
                    diff_value[0],
                ),
            )
        elif diff_type == diff_creator.VALUE_CHILD:
            collected_data.append(build_plain(child, path))
        elif diff_type == diff_creator.VALUE_CHANGED:
            collected_data.append(
                build_string(
                    TEMPLATE_CHANGED,
                    path,
                    diff_value[0],
                    diff_value[1],
                ),
            )
        path.pop()
    return '\n'.join(collected_data)


def build_string(
    template: str,
    path: List,
    value1: str,
    value2: str = None,
) -> str:
    """
    Build result string.

    Args:
        template: template for building string.
        path: path to value.
        value1: old value of diff.
        value2: new value of diff.

    Returns:
        str.
    """
    if template == TEMPLATE_CHANGED:
        return template.format(
            path='.'.join(path),
            value1=build_value(value1),
            value2=build_value(value2),
        )
    return template.format(
        path='.'.join(path),
        value=build_value(value1),
    )


def build_value(diff_value: Any) -> str:
    """
    Build string from value.

    Args:
        diff_value: value of diff.

    Returns:
        str.
    """
    if isinstance(diff_value, dict):
        diff_value = TEMPLATE_COMPLEX_VALUE
    elif isinstance(diff_value, bool):
        diff_value = str(diff_value).lower()
    elif isinstance(diff_value, str):
        diff_value = "'{0}'".format(diff_value)
    elif diff_value is None:
        diff_value = 'null'
    return diff_value
