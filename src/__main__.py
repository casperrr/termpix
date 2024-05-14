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

    

    tool_args = opts.add_subparsers(dest='command')
    tool_parser = tool_args.add_parser('tool', help="Used to use the tpix creation tool")
    tool_parser.add_argument('-f', '--file', type=str, help="File path")
    tool_parser.add_argument('-l', '--link', type=str, help="Image link")
    tool_parser.add_argument('-i', '--interpolation', type=str, help="Interpolation for scaling")
    tool_parser.add_argument('-s', '--scale', nargs=2, type=int, help="Scale (width height)")
    tool_parser.add_argument('-b', '--big-pixels', action='store_true', help="Render with smaller char or larger char")
    tool_parser.add_argument('-q', '--quantization', type=int, help="Color quantization (0-255)")


    args = opts.parse_args()



    print(args)

    # Start
    if args.tool:
        tool = TermpixTool(args)
    else:
        termpix = Termpix()
        # termpix.run()


if __name__ == '__main__':
    main()