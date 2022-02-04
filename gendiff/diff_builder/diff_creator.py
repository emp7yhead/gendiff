"""Functions to build diff tree."""
from typing import Any, Dict, List

VALUE_DELETED = 'deleted'
VALUE_ADDED = 'added'
VALUE_CHANGED = 'changed'
VALUE_UNCHANGED = 'unchanged'
VALUE_CHILD = 'child'


def create_diff(data1: Dict, data2: Dict) -> List[Dict]:
    """
    Create diff of segments.

    Args:
        data1: parsed data from first file.
        data2: parsed data from second file.

    Returns:
        diff: List[dict]
    """
    keys = data1.keys() | data2.keys()
    diff = []
    for key in sorted(keys):
        diff.append(collect_diff_segments(key, data1, data2))
    return diff


def collect_diff_segments(  # noqa: WPS231
    key: str,
    data1: Dict,
    data2: Dict,
) -> Dict:
    """
    Collect diff segment.

    Args:
        key: key of segment
        data1: parsed data from first file.
        data2: parsed data from second file.

    Returns:
        Dict.
    """
    if key not in data1:
        collected_data = create_diff_segment(
            VALUE_ADDED,
            key,
            data2[key],  # noqa: WPS204
        )
    elif key not in data2:
        collected_data = create_diff_segment(
            VALUE_DELETED,
            key,
            data1[key],  # noqa: WPS204
        )
    elif data1[key] == data2[key]:
        collected_data = create_diff_segment(
            VALUE_UNCHANGED,
            key,
            data1[key],
        )
    elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
        collected_data = create_diff_segment(
            VALUE_CHILD,
            key,
            value_old=None,
            child=create_diff(
                data1[key],
                data2[key],
            ),
        )
    else:
        collected_data = create_diff_segment(
            VALUE_CHANGED,
            key,
            value_old=data1[key],
            value_new=data2[key],
        )
    return collected_data


def create_diff_segment(
    diff_type: str,
    key: str,
    value_old: Any,
    value_new: Any = None,
    child: List[Dict] = None,
) -> Dict:
    """
    Create diff segment.

    Args:
        diff_type: type of difference
        key: key of segment
        value_old: old value
        value_new: new value
        child: child (if exists)

    Returns:
        dict.
    """
    return {
        'diff_type': diff_type,
        'key': key,
        'value_old': value_old,
        'value_new': value_new,
        'child': child,
    }


def get_diff_type(collected_data: Dict[str, Any]) -> Any:
    """
    Get diff_type of diff segment.

    Args:
        collected_data: diff segment.

    Returns:
        Any.
    """
    return collected_data.get('diff_type')


def get_key(collected_data):
    """
    Get key of diff segment.

    Args:
        collected_data: diff segment.

    Returns:
        Any.
    """
    return collected_data.get('key')


def get_value(collected_data):
    """
    Get old value and new value of diff segment.

    Args:
        collected_data: diff segment.

    Returns:
        Any.
    """
    return (collected_data.get('value_old'), collected_data.get('value_new'))


def get_child(collected_data):
    """
    Get child of diff segment.

    Args:
        collected_data: diff segment.

    Returns:
        Any.
    """
    return collected_data.get('child', None)
