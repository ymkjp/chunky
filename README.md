chunky.py
===

## Install

- Python 2.7.x

```bash
pip install -r requirements.txt
```

## Usage

```txt
$ python chunky.py --help
usage: chunky.py [-h] --source SOURCE [--destination DESTINATION] [--execute]
                 [--destination-prefix DESTINATION_PREFIX]
                 [--cap N[B,KB,MB,GB]]

Split subdirectories by cap sizes.

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       a source directory containing subdirectories
  --destination DESTINATION
                        a target directory to output subdirectories (default:
                        current directory)
  --execute             To execute copy dirs (default: False)
  --destination-prefix DESTINATION_PREFIX
                        a dir name prefix in dst directory (default: UUID)
  --cap N[B,KB,MB,GB]   Cap size (default: 2GB)
```

## Contribute

PRs accepted.

## License

MIT © Kenta Yamamoto
