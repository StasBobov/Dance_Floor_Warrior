import pygame
from Constants import *
from Human import *


class Player(Human):

    def __init__(self, game):
        super().__init__(game, name='Alcoholic - goer', image='Man.png', size=(75, 116),
                             x_start=START_X, y_start=START_Y, direction=RIGHT, toolbar_image='bars-png.png')
        self.hp = MAX_XP
        self.mp = MAX_MP
        self.toolbar_pack.append(self.toolbar_image.subsurface(235, 0, 192, 20))
