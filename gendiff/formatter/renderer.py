"""Function to render diff in chosen format."""
from typing import Dict, List

from gendiff.formatter.json import build_json
from gendiff.formatter.plain import build_plain
from gendiff.formatter.stylish import build_stylish

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

FORMAT_ERROR = 'Please choose valid format.'


def render_diff(diff: List[Dict], style: str) -> str:
    """Render diff in chosen format.

    Args:
        diff: diff between two files.
        style: format of diff(stylish, plain or json)

    Returns:
        str.

    Raises:
        NameError: if style is not supported.
    """
    if style == FORMAT_STYLISH:
        return build_stylish(diff)
    elif style == FORMAT_PLAIN:
        return build_plain(diff)
    elif style == FORMAT_JSON:
        return build_json(diff)
    raise NameError(FORMAT_ERROR)
