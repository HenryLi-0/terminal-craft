from subsystems.mathutil import *
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
    def setPixel(self, x, y, color):
        self.data[y][x] = color
    def getPixel(self, x, y):
        return self.data[y][x]

class Display:
    @staticmethod
    def color(foreground, background):
        return "\033[38;2;{};{};{};48;2;{};{};{}m".format(minmax(0, round(foreground[0]), 255), minmax(0, round(foreground[1]), 255), minmax(0, round(foreground[2]), 255), minmax(0, round(background[0]), 255), minmax(0, round(background[1]), 255), minmax(0, round(background[2]), 255))
    @staticmethod
    def colorForeground(foreground):
        return "\033[38;2;{};{};{}".format(minmax(0, round(foreground[0]), 255), minmax(0, round(foreground[1]), 255), minmax(0, round(foreground[2]), 255))

    def __init__(self):
        self.tick = 0

    def render(self, data:DisplayData, debug = True):
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
        print("\033[0m" + "Debug: ({}x{}), tick {} | t(all)={}ms, t(render)={}ms, t(clear)={}ms, t(print)={}ms"
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