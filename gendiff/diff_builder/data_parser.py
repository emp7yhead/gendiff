import json
import yaml
from gendiff.diff_builder.data_loader import TYPE_JSON


def parse_data(file_data, file_extension):
    if file_extension == TYPE_JSON:
        return get_data_json(file_data)
    else:
        return get_data_yml(file_data)


def get_data_json(file_path):
    parced_data = json.load(file_path)
    return parced_data


def get_data_yml(file_path):
    parced_data = yaml.safe_load(file_path)
    return parced_data
