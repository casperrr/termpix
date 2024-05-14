#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import os
from PIL import Image
from io import BytesIO
import validators
class TermpixTool:
    def __init__(self, args):
        
        # Check arguments
        self.checkArgs(args)
        
        self.pixArray = []


        # Get image
        if args.file:
            self.img = Image.open(args.file).convert('RGBA')
        elif args.link:
            response = requests.get(self.imgPath)
            self.img = Image.open(BytesIO(response.content)).convert('RGBA')
        else:
            print("idk how an error occured here but it did so my bad")
            exit(5)

        # Scale image
        if args.interpolation:
            self.img.thumbnail((args.scale[0], args.scale[1]), resample=Image.NEAREST)
        else:
            self.img.thumbnail((args.scale[0], args.scale[1]))

        # Quantize Colors  
        self.img = self.img.quantize(colors=args.quantization)

        self.img = self.img.convert('RGBA')
        if args.img_data:
            print(self.img)
        
        # Save the processed image
        if args.save_processed:
            self.img.save(args.save_processed, 'PNG')

        # Populate array with pixels
        self.getPixels()

        self.imgString = self.createImgString()
        if args.hide_result:
            print(self.imgString)

    def getPixels(self):
        pixels = self.img.load()
        imgWidth, imgHeight = self.img.size
        xStep = 1
        yStep = 1

        for y in range(0, imgHeight, yStep):
            row = []
            for x in range(0, imgWidth, xStep):
                pixel = pixels[x, y]
                if isinstance(pixel, int):  # For grayscale images
                    pixel = (pixel, pixel, pixel)
                row.append(pixel)
            self.pixArray.append(row)

    def testPrint2(self):
        for row in self.pixArray:
            for pixel in row:
                r, g, b = pixel
                print(f"\033[38;2;{r};{g};{b}m██", end="")
            print()

    def createImgString(self):
        alphaThresh = 128
        result = ""
        for y in range(0, len(self.pixArray), 2):
            for x in range(len(self.pixArray[0])):
                r1, g1, b1, a1 = self.pixArray[y][x]
                r2, g2, b2, a2 = self.pixArray[y+1][x] if y+1 < len(self.pixArray) else (0, 0, 0, 255)
                if a2 < alphaThresh and a1 < alphaThresh:  # If the pixel is transparent
                    result += ' '
                else:
                    result += f"\033[38;2;{r2};{g2};{b2}m\033[48;2;{r1};{g1};{b1}m▄"
                result += "\033[0m"  # Reset colors after each pixel
            result += '\n'  # Add a newline at the end of each row
        return result
    
    def checkArgs(self, args):
        self.__checkFile(args)
        if(args.scale):
            if args.scale[0] > 255 or args.scale[1] > 255:
                print("Scale is too large recomended scale is <100")
                exit(250)
        if args.quantization > 255:
            print("Color quantization range is between 0-255")
            exit(249)
        if args.save_processed:
            if not os.path.isdir(os.path.dirname(args.save_processed)):
                print(f"Invalid save location: {args.save_processed}")
                exit(1)
            if not os.access(os.path.dirname(args.save_processed), os.W_OK):
                print(f"Save location is not accessible: {args.save_processed}")
                exit(1)

    
    def __checkFile(self, args):
        # Check img provided
        # No image provided at all
        if args.file == None and args.link == None:
            print("No file/link to img provided please use -f or -l.")
            exit(255)
            return
        # Both link and file provided
        if args.file and args.link:
            print("You cant provide link and file arguments please only choose 1")
            exit(254)
            return
        if args.file:
            filePath = args.file
            if not os.path.isfile(filePath):
                print(f"Invalid file path: {filePath}")
                exit(1)
            if not os.access(filePath, os.R_OK):
                print(f"File is not accessible: {filePath}")
                exit(1)
            _, ext = os.path.splitext(filePath)
            if ext.lower() not in ['.png', '.jpeg', '.jpg']:
                print(f"Invalid file type: {filePath}")
                exit(1)
        elif args.link:
            # Check if the link is valid
            if not validators.url(args.link):
                print(f"Invalid link 1: {args.link}")
                exit(1)
            response = requests.head(args.link)
            if response.status_code != 200:
                print(f"Invalid link 2: {args.link}")
                exit(1)