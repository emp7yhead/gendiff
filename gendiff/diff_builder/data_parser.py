"""Functions to parse data from files."""
import json
from typing import Any, Dict

import yaml
from gendiff.diff_builder.data_loader import TYPE_JSON


def parse_data(file_data: str, file_extension: Any) -> Dict:
    """
    Parse data from files depending on the extension.

    Args:
        file_data: data from file.
        file_extension: extension of file.

    Returns:
        Dict
    """
    if file_extension == TYPE_JSON:
        return get_data_json(file_data)
    return get_data_yml(file_data)


def get_data_json(file_path: str) -> Dict:
    """
    Get data from JSON file.

    Args:
        file_path: absolute or relative path to file.

    Returns:
        str.
    """
    return json.loads(file_path)


def get_data_yml(file_path: str) -> Dict:
    """
    Get data from YML or YAML file.

    Args:
        file_path: absolute or relative path to file.

    Returns:
        str.
    """
    return yaml.safe_load(file_path)
