"""Parse a recorded game.


Parses an "mgz" recorded game, extracts notable information,
and computes a variety of useful metadata.
"""

import datetime
import os.path
import re
from collections import defaultdict, Counter

import voobly

import mgz
import mgz.body
import mgz.util

import json


# pylint: disable=too-many-instance-attributes, too-many-arguments
class ParsedGame():
    """Parsed game wrapper."""

    def __init__(self, path, voobly_api_key=None, chat=False, timeline=False, coords=False):
        self._handle = open(path, 'rb')
        self._handle.seek(0, 2)
        self._eof = self._handle.tell()
        self._handle.seek(0)
        self._header = mgz.header.parse_stream(self._handle)
        self._operations = []
        while self._handle.tell() < self._eof:
            operation = mgz.body.operation.parse_stream(self._handle)
            self._operations.append(operation)

    def parseFull(self):
        return {'header': self._header, 'body': self._operations}
