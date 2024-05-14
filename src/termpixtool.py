#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from PIL import Image
from io import BytesIO
class TermpixTool:
    def __init__(self, args):
        if args.tool == "":
            args.help()
            exit(255)
            return
        
        asciiPix = "█"
        self.pixArray = []
        self.imgPath = args.tool

        response = requests.get(self.imgPath)
        self.img = Image.open(BytesIO(response.content)).convert('RGBA')

        self.img.thumbnail((70, 100), resample=Image.NEAREST)
        # self.img.thumbnail((70, 100))
        self.img = self.img.quantize(colors=30)
        self.img = self.img.convert('RGBA')
        print(self.img)
        self.createTPix()

        # Save the processed image
        self.img.save('processed_image.png', 'PNG')

        # print(self.pixArray)
        self.testPrint3()
        self.string = self.testPrint3ToString()
        print(self.string)
        # self.testPrint2()

    def createTPix(self):
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
    
    def testPrint(self):
        for y in range(0, len(self.pixArray), 2):
            for x in range(len(self.pixArray[0])):
                r1, g1, b1 = self.pixArray[y][x]
                r2, g2, b2 = self.pixArray[y+1][x] if y+1 < len(self.pixArray) else (0, 0, 0)
                print(f"\033[38;2;{r2};{g2};{b2}m\033[48;2;{r1};{g1};{b1}m▄", end="")
            print("\033[0m")  # Reset colors
            # if y > 10: return

    def testPrint2(self):
        for row in self.pixArray:
            for pixel in row:
                r, g, b = pixel
                print(f"\033[38;2;{r};{g};{b}m██", end="")
            print()

    def testPrint3(self):
        alphaThresh = 128
        for y in range(0, len(self.pixArray), 2):
            for x in range(len(self.pixArray[0])):
                r1, g1, b1, a1 = self.pixArray[y][x]
                r2, g2, b2, a2 = self.pixArray[y+1][x] if y+1 < len(self.pixArray) else (0, 0, 0, 255)
                if a2 < alphaThresh and a1 < alphaThresh:  # If the pixel is transparent
                    print(' ', end="")
                else:
                    print(f"\033[38;2;{r2};{g2};{b2}m\033[48;2;{r1};{g1};{b1}m▄", end="")
                print("\033[0m", end="")  # Reset colors after each pixel
            print()  # Print a newline at the end of each row

    def testPrint3ToString(self):
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