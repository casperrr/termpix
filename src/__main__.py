#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from termpix import *
from termpixtool import *
from argparse import ArgumentParser

def main():
    opts = ArgumentParser(prog= 'termpix',
                            description= 'Display Ascii art in your terminal',
                            usage= 'This is a test')
    
    opts.add_argument('-m', action="store_true", help="IDK WAHTS GOING ON")
    opts.add_argument('-t', '--tool', type=str, help="Used to use the tpix creation tool")


    args = opts.parse_args()



    print(args)

    # Start
    if args.tool:
        tool = TermpixTool(args.tool)
    else:
        termpix = Termpix()
        # termpix.run()


if __name__ == '__main__':
    main()