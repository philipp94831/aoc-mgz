"""Parse a recorded game.


Parses an "mgz" recorded game, extracts notable information,
and computes a variety of useful metadata.
"""

import mgz
import mgz.body
import mgz.util


# pylint: disable=too-many-instance-attributes, too-many-arguments
class ParsedGame():
    """Parsed game wrapper."""

    def __init__(self, handle):
        self._handle = handle
        self._handle.seek(0, 2)
        self._eof = self._handle.tell()
        self._handle.seek(0)
        self._header = mgz.header.parse_stream(self._handle)
        self._operations = []
        while self._handle.tell() < self._eof:
            operation = mgz.body.operation.parse_stream(self._handle)
            self._operations.append(operation)

    def parse_full(self):
        return {'header': self._header, 'body': self._operations}
