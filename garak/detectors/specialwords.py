#!/usr/bin/env python3
"""
Specialwords detectors

Matches terms in word lists
"""


import json

import garak._config
from garak.detectors.base import StringDetector


class SlursReclaimedSlurs(StringDetector):
    description = "Slurs and reclaimed slurs"
    uri = "https://en.wikipedia.org/wiki/List_of_ethnic_slurs"
    bcp47 = "en"
    tags = [
        "avid-effect:ethics:E0101",
        "avid-effect:ethics:E0301",
        "avid-effect:ethics:E0302",
        "avid-effect:performance:P0401",
    ]

    def __init__(self):
        self.substrings = set([])
        with open(
            garak._config.basedir / "resources/slurprompts.jsonl", "r"
        ) as slurfile:
            for line in slurfile:
                line = line.strip()
                if not line:
                    continue
                self.substrings.add(json.loads(line)["term"])

        super().__init__(self.substrings)
        self.matchtype = "word"
