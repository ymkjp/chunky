chunky.py
===

## Install

- Python 2.7.x

```bash
pip install -r requirements.txt
```

## Usage
#### Quick start

```bash
python chunky.py --source ${__PATH_TO_TARGET_DIR__} --cap 2GB  # Dry-run
python chunky.py --source ${__PATH_TO_TARGET_DIR__} --cap 2GB --execute
```

* Then `chunky.py` creates a directory named by UUID such as `9354afcd-7e3f-446f-844c-db97b04a5435/` to your current directory
* Within the directory, it contains directories named by index such as `0/`, `1/`, `2/` and each of them:
    * has smaller size than given cap (2GB in this example)
    * contaions copied sub-directories under the `__PATH_TO_TARGET_DIR__`

```txt
$ du -sh 9354afcd-7e3f-446f-844c-db97b04a5435/* | tail -n3
1.8G    0/
2.0G    1/
1.3G    2/
```

As you see, `chuncky.py` has the different feature from [split\(1\)](http://man7.org/linux/man-pages/man1/split.1.html).

#### Options
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
