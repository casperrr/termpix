#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from termpix import Termpix, TermpixTool
from argparse import ArgumentParser

def main():
    opts = ArgumentParser(prog= 'termpix',
                          description= 'Display Ascii art in your terminal',
                          usage= 'termpix [options] \n       ' \
                                  'termpix tool [tool-options]')

    opts.add_argument('-l', '--list', action='store_true', help='List available termpix file names')
    opts.add_argument('-L', '--list-imgs', action='store_true', help='List available termpix images')
    opts.add_argument('-s', '--select', type=str, help='Select a specific termpix file to display')
    opts.add_argument('-d', '--directory', type=str, help='Select a custom directory to search for termpix files')
    opts.add_argument('-f', '--file', type=str, help='Select a specific termpix file path to display')

    tool_args = opts.add_subparsers(dest='command')
    tool_parser = tool_args.add_parser('tool', help="Used to use the tpix creation tool")
    tool_parser.add_argument('-f', '--file', type=str, help="File path")
    tool_parser.add_argument('-l', '--link', type=str, help="Image link")
    tool_parser.add_argument('-o', '--output-location', type=str, help="Output Location of resulting file")
    tool_parser.add_argument('-i', '--interpolation', action='store_true', help="Interpolation for scaling (adding -i will enable it)")
    tool_parser.add_argument('-t', '--thresh', type=int, default=128, help="Threshold for background transparency (0-256)")
    tool_parser.add_argument('-s', '--scale', nargs=2, type=int, default=[70, 100] ,help="Scale (width height)")
    # tool_parser.add_argument('-b', '--big-pixels', action='store_true', help="Render with smaller char or larger char") # Not implemented yet and i cant really be bothered
    tool_parser.add_argument('-q', '--quantization', type=int, default=255, help="Color quantization (0-255)")
    tool_parser.add_argument('-r', '--hide-result', action='store_false', help="Hide the output of the image")
    tool_parser.add_argument('--save-processed', type=str, help="Path of where to save processed image")
    tool_parser.add_argument('--img-data', action='store_true', help="Print data about the image")
    # add another one that will try and remove the background from an image by using the 0,0 pixel color 

    args = opts.parse_args()

    # print(args) # debug

    # Start
    if args.command == 'tool':
        tool = TermpixTool(args)
    else:
        termpix = Termpix(args)
        # termpix.run()


if __name__ == '__main__':
    main()