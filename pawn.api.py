#!/usr/bin/env python
#
# This script generates API files from includes.
#
# Use it as following:
#   find pawno/include -name "*.inc" | xargs python pawn.api.py | sort > pawn.api

import re
import sys

def main(argv):
  for filename in argv[1:]:
    with open(filename, 'r') as f:
      for line in f.readlines():
        match = re.match(r'(?:forward|native)\s+(?:\S+:\s*)?(\S+\s*\(.*?\))\s*;',
                         line, re.MULTILINE)
        if match is not None:
          print(match.group(1).translate(None, '\r\n'))

if __name__ == '__main__':
  sys.exit(main(sys.argv))
