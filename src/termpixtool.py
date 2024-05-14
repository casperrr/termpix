from PIL import Image

class TermpixTool:
    def __init__(self, args):
        if args.tool == "":
            args.help()
            exit(255)
            return
        
        asciiPix = "█"
        self.pixArray = []
        self.imgPath = args.tool
        self.img = Image.open(self.imgPath)
        print(self.img)
        self.createTPix()

        # print(self.pixArray)
        self.testPrint()

    def createTPix(self):
        pixels = self.img.load()
        imgWidth, imgHeight = self.img.size
        xStep = 1
        yStep = 1

        # print(imgHeight, imgHeight)

        
        for y in range(0, imgHeight, yStep):
            row = []
            for x in range(0, imgWidth, xStep):
                pixel = pixels[x, y]
                row.append(pixel)
            self.pixArray.append(row)
    
    def testPrint(self):
        for y in range(0, len(self.pixArray), 2):
            for x in range(len(self.pixArray[0])):
                r1, g1, b1 = self.pixArray[y][x]
                r2, g2, b2 = self.pixArray[y+1][x] if y+1 < len(self.pixArray) else (0, 0, 0)
                print(f"\033[38;2;{r1};{g1};{b1}m\033[48;2;{r2};{g2};{b2}m▄", end="")
            print("\033[0m")  # Reset colors
