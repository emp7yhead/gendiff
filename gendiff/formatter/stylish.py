from gendiff.program import diff_creator

INDENT_COUNT = 4
INDENT_SYMBOL = ' '

TEMPLATE_FORM = '{indent}{diff_symbol} {key}: {value}'

SYMBOL_ADDED = '+'
SYMBOL_DELETED = '-'
SYMBOL_UNCHANGED = ' '


def build_stylish(tree, depth=1):

    data = []
    data.append('{')

    spaces = build_spaces(depth)
    opening_indent = INDENT_SYMBOL * spaces

    for node in tree:

        status = diff_creator.get_status(node)
        key = diff_creator.get_key(node)
        value = diff_creator.get_value(node)
        child = diff_creator.get_child(node)

        if status == diff_creator.VALUE_DELETED:
            string = build_string(opening_indent,
                                  SYMBOL_DELETED,
                                  key,
                                  build_value(value[0],
                                              depth + 1))

        elif status == diff_creator.VALUE_ADDED:
            string = build_string(opening_indent,
                                  SYMBOL_ADDED,
                                  key,
                                  build_value(value[0],
                                              depth + 1))

        elif status == diff_creator.VALUE_UNCHANGED:
            string = build_string(opening_indent,
                                  SYMBOL_UNCHANGED,
                                  key,
                                  build_value(value[0],
                                              depth + 1))

        elif status == diff_creator.VALUE_CHILD:
            string = build_string(opening_indent,
                                  SYMBOL_UNCHANGED,
                                  key,
                                  build_stylish(child,
                                                depth + 1))

        else:
            string_old = build_string(opening_indent,
                                      SYMBOL_DELETED,
                                      key,
                                      build_value(value[0],
                                                  depth + 1))
            string = string_old + '\n' + build_string(opening_indent,
                                                      SYMBOL_ADDED,
                                                      key,
                                                      build_value(value[1],
                                                                  depth + 1))
        data.append(string)
    data.append(INDENT_SYMBOL * (spaces - 2) + '}')
    return '\n'.join(data)


def build_value(item, depth):

    template = []
    spaces = build_spaces(depth)
    opening_indent = INDENT_SYMBOL * spaces

    if isinstance(item, dict):
        template.append('{')
        for key, value in item.items():
            template.append(build_string(opening_indent,
                                         SYMBOL_UNCHANGED,
                                         key,
                                         build_value(value,
                                                     depth + 1)))
        template.append(INDENT_SYMBOL * (spaces - 2) + '}')
    elif isinstance(item, bool):
        template.append(str(item).lower())
    elif item is None:
        template.append('null')
    else:
        template.append(str(item))

    return '\n'.join(template)


def build_string(indent, symbol, key, value):
    return TEMPLATE_FORM.format(indent=indent,
                                diff_symbol=symbol,
                                key=key,
                                value=value)


def build_spaces(depth):
    spaces = INDENT_COUNT * depth - 2
    return spaces
