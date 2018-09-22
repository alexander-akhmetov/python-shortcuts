import argparse
import os.path

from shortcuts import Shortcut
from shortcuts.utils import (
    convert_plist_to_xml,
    convert_plist_to_binary,
)


def convert_shortcut(input_filepath, out_filepath):
    input_format = _get_format(input_filepath)
    out_format = _get_format(out_filepath)

    if input_format == 'plist':
        convert_plist_to_xml(input_filepath)

    with open(input_filepath, 'rb') as f:
        sc = Shortcut.load(f, file_format=input_format)
    with open(out_filepath, 'w') as f:
        sc.dump(f, file_format=out_format)

    if out_format == 'plist':
        convert_plist_to_binary(out_filepath)


def _get_format(filepath):
    _, ext = os.path.splitext(filepath)
    ext = ext.strip('.')
    if ext in ('shortcut', 'plist'):
        return 'plist'
    elif ext == 'toml':
        return 'toml'

    raise RuntimeError(f'Unsupported file format: {filepath}: "{ext}"')


def main():
    parser = argparse.ArgumentParser(description='Shortcuts: Siri shortcuts creator')
    parser.add_argument('file', help='shortcut source file')
    parser.add_argument('output', help='shortcut output file')

    args = parser.parse_args()

    convert_shortcut(args.file, args.output)


if __name__ == '__main__':
    main()
