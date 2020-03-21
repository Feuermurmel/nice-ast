# nice-ast

`nice-ast` is a command line tool to dump a Python AST in a nicely formatted way.


## Usage

```
$ nice-ast --help
usage: nice-ast [-h] path

Parse a Python file and print the resulting AST in a nice, colorful way.

positional arguments:
  path        Path to the Python file to parse.

optional arguments:
  -h, --help  show this help message and exit
```


## Screen Shot

![Screen shot of output of running nice-ast niceast/__init__.py](doc/screen-shot.png)



## Resources

- [Python: ast — Abstract Syntax Trees](https://docs.python.org/3/library/ast.html)
- [Green Tree Snakes - the missing Python AST docs](https://greentreesnakes.readthedocs.io/)


## Development Setup

```
python3 -m venv venv
. venv/bin/activate
pip install -e '.[dev]'
```
