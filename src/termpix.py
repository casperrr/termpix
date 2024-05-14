#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


class Termpix():

    def __init__(self):
        '''
        Constructor
        '''
        # The user's home directory
        self.HOME = os.environ['HOME'] if 'HOME' in os.environ else ''
        if len(self.HOME) == 0:
            os.environ['HOME'] = self.HOME = os.path.expanduser('~')