TYPE_JSON = '.json'
TYPE_YML_OR_YAML = ('.yml', '.yaml')

FILE_ERROR = 'Please choose valid file.'


def get_file_data_and_extension(file_path):
    if file_path.endswith(TYPE_JSON):
        file_extension = TYPE_JSON
    elif file_path.endswith(TYPE_YML_OR_YAML):
        file_extension = TYPE_YML_OR_YAML
    else:
        raise NameError(FILE_ERROR)
    file_data = open(file_path, 'r')
    return file_data, file_extension
