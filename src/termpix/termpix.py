#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import random
from pathlib import Path
import sys

class Termpix():

    def __init__(self):
        '''
        Constructor
        '''
        # The user's home directory
        self.HOME = os.environ['HOME'] if 'HOME' in os.environ else ''
        if len(self.HOME) == 0:
            os.environ['HOME'] = self.HOME = os.path.expanduser('~')

        print(self.HOME)

        self.tpix_path = self._find_tpix_path()
        self.testRun()

    def _find_tpix_path(self):
        search_paths = [
            Path(sys.prefix) / "share/termpix/tpix",
            Path(__file__).parent.parent.parent / "tpix",
            Path("/usr/share/termpix/tpix"),
            Path.home() / ".local/share/termpix/tpix",
        ]
        for path in search_paths:
            if path.exists():
                return path
        raise FileNotFoundError(f"tpix directory not found. Searched: {[str(p) for p in search_paths]}")

    def testRun(self):
        # path = "/share/termpix/tpix/"
        path = self.tpix_path
        files = os.listdir(path)
        files = [f for f in files if os.path.isfile(os.path.join(path, f))]
        if files:
            random_file = random.choice(files)
            print(f"Random file: {random_file}")
            with open(os.path.join(path, random_file), 'r') as f:
                file_contents = f.read()
            print(file_contents)
        else:
            print("No files found in the directory.")
