import sys
import json
from mgz.parsed_game import ParsedGame
import os
from os import listdir
from os.path import isfile, join, exists
import construct

def parse(f, parsefile):
    game = ParsedGame(f)
    parsed = game.parseFull()
    with open(parsefile, "w") as out:
       out.write(json.dumps(parsed, sort_keys=True))

if __name__ == "__main__":
    construct.setglobalstringencoding('latin1')
    mypath = sys.argv[1]
    onlyfiles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(mypath) for f in filenames if f.endswith('.mgz')]
    for f in onlyfiles:
        base = ('.').join(f.split('.')[:-1])
        parsefile = base + ".full.json"
        if not exists(parsefile):
            print("parsing " + f)
            parse(f, parsefile)

    print("Finished")
