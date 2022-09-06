import pygame
from Constants import *
from Human import *


class NPC(Human):

    def __init__(self, game, image, name, size):
        super().__init__(game, image, name, size, x_start=350, y_start=200, direction=LEFT, toolbar_image='bar_20x50')
        self.hp = MAX_XP
        self.mp = MAX_MP
        self.toolbar_pack = []
        self.moving = [0, 0, 0, 0]
        self.toolbar_image = pygame.image.load('bars-png.png').convert_alpha()
        self.toolbar_pack.append(self.toolbar_image)

    def move(self):
        if self.moving[RIGHT] == 1:
            self.x += PLAYER_SPEED
        if self.moving[LEFT] == 1:
            self.x -= PLAYER_SPEED
        if self.moving[UP] == 1:
            self.y -= PLAYER_SPEED
        if self.moving[DOWN] == 1:
            self.y += PLAYER_SPEED

        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > SCREEN_WIDTH - 75:  self.x = SCREEN_WIDTH - 75
        if self.y > SCREEN_HEIGHT - 116: self.y = SCREEN_HEIGHT - 116





    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(self.toolbar_pack[0], (950, 15))
        m = 1
        z = self.hp // 2


class Chick(NPC):

    def __init__(self, game):
        super().__init__(game, image='chick.png', name='Chick', size = (75, 150))
