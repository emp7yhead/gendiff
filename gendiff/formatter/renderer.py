from gendiff.formatter.stylish import build_stylish
from gendiff.formatter.plain import build_plain
from gendiff.formatter.json import build_json

FORMAT_STYLISH = 'stylish'
FORMAT_PLAIN = 'plain'
FORMAT_JSON = 'json'

FORMAT_ERROR = 'Please choose valid format.'


def render_diff(diff, style):
    if style == FORMAT_STYLISH:
        return build_stylish(diff)
    elif style == FORMAT_PLAIN:
        return build_plain(diff)
    elif style == FORMAT_JSON:
        return build_json(diff)
    else:
        raise NameError(FORMAT_ERROR)
