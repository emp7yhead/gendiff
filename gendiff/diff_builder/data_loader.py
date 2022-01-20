TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')

FILE_ERROR = 'Please choose valid file.'


def get_file_data(file_path):
    with open(file_path, 'r') as file_data:
        return file_data.read()


def get_file_extension(file_path):
    if file_path.endswith(TYPE_JSON):
        file_extension = TYPE_JSON
    elif file_path.endswith(TYPE_YML_OR_YAML):
        file_extension = TYPE_YML_OR_YAML
    else:
        raise NameError(FILE_ERROR)
    return file_extension


def get_file_data_and_extension(file_path):
    file_data = get_file_data(file_path)
    file_extension = get_file_extension(file_path)
    return file_data, file_extension
