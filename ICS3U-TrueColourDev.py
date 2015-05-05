"""Import base functiosn and modules"""
import os, sys
import math
from random import random, randint
import pygame
from pygame.locals import *
import tempfile
from time import sleep

"""Loading of game window, base colours, and sizing presets. Screen size will be defaulted at 800x800 pixels"""
white = (255, 255, 255)
black = (0, 0, 0)
window = (800, 800)

"""Level based colours
The game will be based on 3 "hidden" levels of skill. Depending on how many points are achieved, extra colours may be added to confuse and challenge the
users. Points will be awarded per correct answer. Upon game restart (whether from failure to select correct answer or full restart), the points will be
reset as well. Smiley face :)."""
#Hidden Level One colours : Base
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 102, 0)
blue = (0, 0, 255)
purple = (127, 0, 255)

#Hidden Level Two colours : Neon/Pastel
cyan = (0, 255, 255)
fuschia = (255, 0, 255)
lime = (128, 255, 0)
pink = (255, 153, 255)


#Hidden Level Three colours : Shades
brown = (139, 69, 19)
grey = (128, 128, 128)

