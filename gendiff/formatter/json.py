"""Function to build json for diff."""
import json
from typing import Dict, List


def build_json(diff: List[Dict]) -> str:
    """
    Build diff in json format.

    Args:
        diff: diff tree between two files.

    Returns:
        str
    """
    return json.dumps(diff, indent=4)
