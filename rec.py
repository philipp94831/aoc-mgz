import json
import os
import sys
import traceback
from os import path

import construct

from mgz.parsed_game import ParsedGame


def parse(file_name: str):
    try:
        with open(file_name, 'rb') as handle:
            game = ParsedGame(handle)
            return game.parse_full()
    except Exception:
        print("Error parsing")
        traceback.print_exc(file=sys.stderr)
        return None


def get_base_name(file_name: str) -> str:
    return '.'.join(file_name.split('.')[:-1])


def find_files(path_name: str):
    yield from (path.join(directory, file_name) for directory, _, file_names in os.walk(path_name) for file_name in
                file_names)


def find_mgz_files(path_name: str):
    yield from (file_name for file_name in find_files(path_name) if file_name.endswith('.mgz'))


def parse_in_directory(path_name: str):
    construct.setglobalstringencoding('latin1')
    files = find_mgz_files(path_name)
    for file in files:
        base = get_base_name(file)
        json_file = '{0}.full.json'.format(base)
        if not path.exists(json_file):
            print("parsing " + file)
            parsed = parse(file)
            if parsed:
                try:
                    json_string = json.dumps(parsed)
                    with open(json_file, "w") as out:
                        out.write(json_string)
                except Exception:
                    print("Error writing")
                    traceback.print_exc(file=sys.stderr)
    print("Finished")


if __name__ == "__main__":
    p = sys.argv[1]
    parse_in_directory(p)
