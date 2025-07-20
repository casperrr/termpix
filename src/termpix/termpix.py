#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
from pathlib import Path
import sys
import sysconfig

class Termpix():

    def __init__(self):
        self.tpix_path = Path(sysconfig.get_path('data')) / "share/termpix/tpix"
        self.testRun()

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
