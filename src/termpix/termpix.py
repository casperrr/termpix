#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import random

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
        self.testRun()

    def testRun(self):
        path = "/usr/share/termpix/tpix/"
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
