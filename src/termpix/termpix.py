#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import random
from pathlib import Path
import sys
import sysconfig

class Termpix():

    def __init__(self, args):
        self._validate_args(args)

        self.tpix_path = Path(sysconfig.get_path('data')) / "share/termpix/tpix"
        if args.directory and os.path.isdir(args.directory):
            self.tpix_path = Path(args.directory)

        self.files = self.get_tpix(self.tpix_path)

        # List options
        if args.list or args.list_imgs:
            for f in self.files:
                print(f[:-5])
                if args.list_imgs: self.display_tpix(f)
            return

        # File select
        if args.file:
            if os.path.isfile(os.path.join(self.tpix_path, args.file)) and args.file.endswith('.tpix'):
                self.display_tpix(args.file)
                return
            else:
                print(f"File '{args.file}' does not exist or is not a .tpix file.")
                exit(1)

        # Select
        if args.select:
            if args.select+'.tpix' in self.files:
                self.display_tpix(args.select+'.tpix')
                return
            else:
                print(f'TPix file {args.select} not found.')
                exit(1)

        self.display_tpix(random.choice(self.files))


        # self.testRun()

    def _validate_args(self, args):
        if args.directory:
            if not os.path.dirname(args.directory):
                print(f'Invalid directory: {args.directory}')
        # Right cant be arsed to do the rest of this

    def get_tpix(self, path):
        return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.tpix')]

    def display_tpix(self, file):
        with open(os.path.join(self.tpix_path, file), 'r') as f:
            print(f.read())

    def testRun(self):
        path = self.tpix_path
        files = os.listdir(path)
        files = [f for f in files if os.path.isfile(os.path.join(path, f)) and f.endswith('.tpix')]
        if files:
            random_file = random.choice(files)
            print(f"Random file: {random_file}")
            with open(os.path.join(path, random_file), 'r') as f:
                file_contents = f.read()
            print(file_contents)
        else:
            print("No files found in the directory.")
