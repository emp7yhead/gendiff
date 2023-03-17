### Tests and linter status:
[![Maintainability](https://api.codeclimate.com/v1/badges/020f403c6131e21f36b5/maintainability)](https://codeclimate.com/github/emp7yhead/python-project-lvl2/maintainability) [![Test Coverage](https://api.codeclimate.com/v1/badges/020f403c6131e21f36b5/test_coverage)](https://codeclimate.com/github/emp7yhead/python-project-lvl2/test_coverage) [![Check lint & tests](https://github.com/emp7yhead/python-project-lvl2/actions/workflows/check_lint_%20tests.yml/badge.svg)](https://github.com/emp7yhead/python-project-lvl2/actions/workflows/check_lint_%20tests.yml) [![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
# gendiff
## Description:
CLI utilite that shows difference between two JSON or YML files

## Dependencies:
- python = "^3.9"
- pytest = "^6.2.5"
- PyYAML = "^6.0"

## Usage:
```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Generate diff

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show help message and exit
  -f, --format          set format of output
```

## Installation:
### Use the package manager pip:
```
pip install --user git+https://github.com/emp7yhead/python-project-lvl2
```
### Or
### Clone repository and use poetry:
```
git clone https://github.com/emp7yhead/python-project-lvl2
cd python-project-lvl2
make build
make package-install
```

## Work Process
- JSON:

[![asciicast](https://asciinema.org/a/nuZbBzG5Xmbn4gVdiCg4gdR7l.svg)](https://asciinema.org/a/nuZbBzG5Xmbn4gVdiCg4gdR7l)

- YAML:

[![asciicast](https://asciinema.org/a/7pKkiN4ZfeGYwUBGN2h0YGoEe.svg)](https://asciinema.org/a/7pKkiN4ZfeGYwUBGN2h0YGoEe)

- Nested output:

[![asciicast](https://asciinema.org/a/CRB7zYQfEtsBp2bR8OPOTsdGA.svg)](https://asciinema.org/a/CRB7zYQfEtsBp2bR8OPOTsdGA)

- Plain output:

[![asciicast](https://asciinema.org/a/8B4UBx3UdWxhaTnnwLiqqg14a.svg)](https://asciinema.org/a/8B4UBx3UdWxhaTnnwLiqqg14a)

- JSON output:

[![asciicast](https://asciinema.org/a/Hj2e0cUpXz4FuOLlMTy1yibCx.svg)](https://asciinema.org/a/Hj2e0cUpXz4FuOLlMTy1yibCx)
