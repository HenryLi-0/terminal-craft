from subsystems.mathutil import *
from subsystems.debug import *
import random, time, math, numpy
import os, platform

class DisplaySettings:
    WIDTH = 125
    HEIGHT = 30
    ASPECT_RATIO = WIDTH/HEIGHT
    PIXEL = "▀"

class DisplayData:
    @staticmethod
    def generateRandom():
        temp = DisplayData()
        for ie in range(DisplaySettings.HEIGHT):
            for i in range(DisplaySettings.WIDTH):
                temp.setPixel(i, ie, (random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        return temp
    
    def __init__(self):
        self.data = numpy.zeros((DisplaySettings.HEIGHT, DisplaySettings.WIDTH, 3), numpy.uint8)
        self.depthBuffer = numpy.full((DisplaySettings.HEIGHT, DisplaySettings.WIDTH), float("inf"))
    def setPixel(self, x, y, color, distance):
        tempX = round(x)
        tempY = round(y)
        if 0 <= tempX < DisplaySettings.WIDTH and 0 <= tempY < DisplaySettings.HEIGHT:
            if self.depthBuffer[tempY][tempX] > distance:
                self.data[tempY][tempX] = color
                self.depthBuffer[tempY][tempX] = distance
                return True
        return False
    def getPixel(self, x, y):
        return self.data[y][x]
    def reset(self):
        self.data.fill(0)
        self.depthBuffer.fill(float("inf"))

class Display:
    @staticmethod
    def color(foreground, background):
        return "\033[38;2;{};{};{};48;2;{};{};{}m".format(minmax(0, round(foreground[0]), 255), minmax(0, round(foreground[1]), 255), minmax(0, round(foreground[2]), 255), minmax(0, round(background[0]), 255), minmax(0, round(background[1]), 255), minmax(0, round(background[2]), 255))
    @staticmethod
    def colorForeground(foreground):
        return "\033[38;2;{};{};{}".format(minmax(0, round(foreground[0]), 255), minmax(0, round(foreground[1]), 255), minmax(0, round(foreground[2]), 255))

    def __init__(self, debug:Debug):
        self.tick = 0
        self.debug = debug

    def render(self, data:DisplayData):
        start = time.time()
        out = ""
        for ie in range(math.floor(DisplaySettings.HEIGHT/2)):
            for i in range(DisplaySettings.WIDTH):
                out += Display.color(data.getPixel(i, ie*2), data.getPixel(i, ie*2+1)) + DisplaySettings.PIXEL
            out += "\n"
        if DisplaySettings.HEIGHT % 2 == 1:
            for i in range(DisplaySettings.WIDTH):
                out += Display.colorForeground(data.getPixel(i, ie*2)) + DisplaySettings.PIXEL
            out += "\n'"
        endRender = time.time()
        os.system("cls" if platform.system() == "Windows" else "clear")
        endClear = time.time()
        print(out)
        endPrint = time.time()
        self.debug.post(" | Display: ({}x{}), tick {} | t(all)={}ms, t(render)={}ms, t(clear)={}ms, t(print)={}ms"
            .format(
                DisplaySettings.WIDTH,
                DisplaySettings.HEIGHT,
                self.tick,
                roundf((endPrint-start)*1000, 2),
                roundf((endRender-start)*1000, 2),
                roundf((endClear-endRender)*1000, 2),
                roundf((endPrint-endClear)*1000, 2)
            )
        )
        self.tick += 1