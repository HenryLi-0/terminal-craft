from subsystems.mathutil import *
import random, time, math
import os, platform

class DisplaySettings:
    WIDTH = 125
    HEIGHT = 30
    PIXEL = "▀"

class DisplayData:
    @staticmethod
    def generateRandom():
        temp = DisplayData()
        temp.data = [[[random.randint(0,255),random.randint(0,255),random.randint(0,255)] for i in range(DisplaySettings.WIDTH)] for ie in range(DisplaySettings.HEIGHT)]
        return temp
    
    def __init__(self):
        self.data = [[[0,0,0] for i in range(DisplaySettings.WIDTH)] for ie in range(DisplaySettings.HEIGHT)]
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
        self.lastRenderTime = 0

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
        out += "\033[0m" + "Debug: ( {} x {} ), t = {} ms".format(DisplaySettings.WIDTH, DisplaySettings.HEIGHT, roundf(self.lastRenderTime*1000, 2))
        os.system("cls" if platform.system() == "Windows" else "clear")
        print(out)
        end = time.time()
        self.lastRenderTime = end - start