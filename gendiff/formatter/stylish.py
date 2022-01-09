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
    opening_indent = INDENT_SYMBOL * (INDENT_COUNT * depth - 2)
    closing_indent = INDENT_SYMBOL * (INDENT_COUNT * (depth - 1))

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
    data.append(closing_indent + '}')
    return '\n'.join(data)


def build_value(item, depth):

    template = []
    opening_indent = build_opening_indent(depth)
    closing_indent = build_closing_indent(depth)

    if isinstance(item, dict):
        template.append('{')
        for key, value in item.items():
            template.append(build_string(opening_indent,
                                         SYMBOL_UNCHANGED,
                                         key,
                                         build_value(value,
                                                     depth + 1)))
        template.append(closing_indent + '}')
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


def build_opening_indent(depth):
    opening_indent = INDENT_SYMBOL * (INDENT_COUNT * depth - 2)
    return opening_indent


def build_closing_indent(depth):
    closing_indent = INDENT_SYMBOL * (INDENT_COUNT * (depth - 1))
    return closing_indent
