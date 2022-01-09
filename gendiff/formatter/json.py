import json


def build_json(tree):
    return json.dumps(tree, indent=4)
