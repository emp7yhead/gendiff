"""Functions to build stylish format for diff."""
from typing import Any

from gendiff.diff_builder import diff_creator

INDENT_COUNT = 4
INDENT_SYMBOL = ' '

TEMPLATE_FORM = '{0}{1} {2}: {3}'
CLOSING_STRING_FORM = '{0}}}'
CHANGED_VALUE_FORM = '{0}\n{1}'

SYMBOL_ADDED = '+'
SYMBOL_DELETED = '-'
SYMBOL_UNCHANGED = ' '


def build_stylish(  # noqa: WPS210, WPS231
    diff: Any,
    depth: int = 1,
) -> str:
    """
    Build stylish diff.

    Args:
        diff: diff tree between two files.
        depth: nesting depth.

    Returns:
        str.
    """
    collected_data = []
    collected_data.append('{')
    spaces = build_spaces(depth)
    opening_indent = INDENT_SYMBOL * spaces
    for node in diff:

        diff_type = diff_creator.get_diff_type(node)
        key = diff_creator.get_key(node)
        diff_value = diff_creator.get_value(node)
        child = diff_creator.get_child(node)

        if diff_type == diff_creator.VALUE_DELETED:
            string = build_string(
                opening_indent,
                SYMBOL_DELETED,
                key,
                build_value(
                    diff_value[0],
                    depth + 1,  # noqa: WPS204
                ),
            )

        elif diff_type == diff_creator.VALUE_ADDED:
            string = build_string(
                opening_indent,
                SYMBOL_ADDED,
                key,
                build_value(
                    diff_value[0],
                    depth + 1,
                ),
            )

        elif diff_type == diff_creator.VALUE_UNCHANGED:
            string = build_string(
                opening_indent,
                SYMBOL_UNCHANGED,
                key,
                build_value(
                    diff_value[0],
                    depth + 1,
                ),
            )

        elif diff_type == diff_creator.VALUE_CHILD:
            string = build_string(
                opening_indent,
                SYMBOL_UNCHANGED,
                key,
                build_stylish(
                    child,
                    depth + 1,
                ),
            )

        else:
            string_old = build_string(
                opening_indent,
                SYMBOL_DELETED,
                key,
                build_value(
                    diff_value[0],
                    depth + 1,
                ),
            )
            string_new = build_string(
                opening_indent,
                SYMBOL_ADDED,
                key,
                build_value(
                    diff_value[1],
                    depth + 1,
                ),
            )
            string = CHANGED_VALUE_FORM.format(string_old, string_new)

        collected_data.append(string)
    collected_data.append(CLOSING_STRING_FORM.format(
        INDENT_SYMBOL * (spaces - 2),
    ),
    )
    return '\n'.join(collected_data)


def build_value(diff_value: Any, depth: int) -> str:
    """
    Build string from value.

    Args:
        diff_value: value of diff.
        depth: nesting depth.

    Returns:
        str.
    """
    template = []
    spaces = build_spaces(depth)
    opening_indent = INDENT_SYMBOL * spaces

    if isinstance(diff_value, dict):
        template.append('{')
        for key, dict_value in diff_value.items():
            template.append(
                build_string(
                    opening_indent,
                    SYMBOL_UNCHANGED,
                    key,
                    build_value(
                        dict_value,
                        depth + 1,
                    ),
                ),
            )
        template.append(
            CLOSING_STRING_FORM.format(INDENT_SYMBOL * (spaces - 2)),
        )
    elif isinstance(diff_value, bool):
        template.append(str(diff_value).lower())
    elif diff_value is None:
        template.append('null')
    else:
        template.append(str(diff_value))

    return '\n'.join(template)


def build_string(indent: str, symbol: str, key: str, diff_value: Any) -> str:
    """
    Build result string.

    Args:
        indent: indent for string.
        symbol: symbol of diff.
        key: key of diff.
        diff_value: value of diff.

    Returns:
        str.
    """
    return TEMPLATE_FORM.format(
        indent,
        symbol,
        key,
        diff_value,
    )


def build_spaces(depth: int) -> int:
    """
    Build spaces for indent in string.

    Args:
        depth: nesting depth.

    Returns:
        str.
    """
    return INDENT_COUNT * depth - 2
