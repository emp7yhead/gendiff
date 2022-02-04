"""Functions to work with files."""
from typing import Any, Tuple

TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')

FILE_ERROR = 'Please choose valid file.'


def get_file_data(file_path: str) -> str:
    """
    Get data from file.

    Args:
        file_path: absolute or relative path to file.

    Returns:
        str
    """
    with open(file_path, 'r') as file_data:
        return file_data.read()


def get_file_extension(file_path: str) -> Any:
    """
    Get file extension.

    Args:
        file_path: absolute or relative path to file.

    Returns:
        str or tuple.

    Raises:
        NameError: if file extension is not supported.
    """
    if file_path.endswith(TYPE_JSON):
        file_extension = TYPE_JSON
    elif file_path.endswith(TYPE_YML_OR_YAML):
        file_extension = TYPE_YML_OR_YAML
    else:
        raise NameError(FILE_ERROR)
    return file_extension


def get_file_data_and_extension(file_path: str) -> Tuple[str, Any]:
    """
    Get data from file and his extension.

    Args:
        file_path: absolute or relative path to file.

    Returns:
        file_data: str
        file_extension: str or tuple.
    """
    file_data = get_file_data(file_path)
    file_extension = get_file_extension(file_path)
    return file_data, file_extension
