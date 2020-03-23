import argparse
import ast
import pathlib
import sys


def log(message):
    print(message, file=sys.stderr, flush=True)


class UserError(Exception):
    def __init__(self, message, *args):
        super().__init__(message.format(*args))


def parse_args():
    parser = argparse.ArgumentParser(
        description='Parse a Python file and print the resulting AST in a '
                    'nice, colorful way.')

    parser.add_argument(
        '-l',
        '--line-complexity',
        type=int,
        default=7,
        help='Maximum complexity of a node formatted on a single line. Each '
             'node name, field name, and field value or list item is counted '
             'as one. Defaults to 7.',
    )

    parser.add_argument(
        'path',
        type=pathlib.Path,
        help='Path to the Python file to parse.')

    return parser.parse_args()


def format_type(n):
    return f'\x1b[1m{type(n).__name__}\x1b[m'


def format_value(n):
    return f'\x1b[32m{repr(n)}\x1b[m'


def format_one_line(n):
    if isinstance(n, ast.AST):
        res = format_type(n)

        if n._fields:
            values_str = ', '.join(
                f'{i}: {format_one_line(getattr(n, i))}'
                for i in n._fields)

            res += f' {{ {values_str} }}'

        return res
    elif isinstance(n, list):
        elements_str = ', '.join(format_one_line(i) for i in n)

        return f'[{elements_str}]'
    else:
        return format_value(n)


def print_ast(node: ast.AST, max_line_complexity):
    def node_complexity(n):
        if isinstance(n, ast.AST):
            return 1 + sum(1 + node_complexity(getattr(n, i)) for i in n._fields)
        elif isinstance(n, list):
            return sum(node_complexity(i) for i in n)
        elif isinstance(n, str):
            return len(n) // 10 + 1
        else:
            return 1

    def walk_node(n, indent, prefix):
        if node_complexity(n) <= max_line_complexity:
            print(f'{indent}{prefix}{format_one_line(n)}')
        else:
            if isinstance(n, ast.AST):
                print(f'{indent}{prefix}{format_type(n)}')

                for i in n._fields:
                    walk_node(getattr(n, i), indent + '  ', f'{i}: ')
            elif isinstance(n, list):
                print(f'{indent}{prefix}')

                for i in n:
                    walk_node(i, indent + '  ', '- ')
            else:
                print(f'{indent}{prefix}{format_value(n)}')

    walk_node(node, '', '')


def main(path, line_complexity):
    # TODO: Add error handling for parsing errors.
    print_ast(ast.parse(path.read_bytes(), str(path)), line_complexity)


def entry_point():
    try:
        main(**vars(parse_args()))
    except KeyboardInterrupt:
        log('Operation interrupted.')
        sys.exit(1)
    except UserError as e:
        log(f'error: {e}')
        sys.exit(2)
