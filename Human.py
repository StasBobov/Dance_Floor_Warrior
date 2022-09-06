import pygame
from Constants import *


class Human:

    def __init__(self, game, name, image, size, x_start, y_start, direction, toolbar_image):
        self.game = game
        self.state = ALIVE
        self.x = x_start
        self.y = y_start
        self.direction = direction
        self.name = name
        self.size = size
        self.blocked = [0, 0, 0, 0]
        self.moving = [0, 0, 0, 0]
        self.image = pygame.image.load(image).convert_alpha()
        self.toolbar_image = pygame.image.load(toolbar_image).convert_alpha()
        self.toolbar_pack = []


    def __str__(self):
        return f'{self.name}  {str(self.x)} {str(self.y)}'

    def move(self):
        self.block_check()
        if self.moving[RIGHT] == 1 and self.blocked[RIGHT] == 0:
            self.x += PLAYER_SPEED
        if self.moving[LEFT] == 1 and self.blocked[LEFT] == 0:
            self.x -= PLAYER_SPEED
        if self.moving[UP] == 1 and self.blocked[UP] == 0:
            self.y -= PLAYER_SPEED
        if self.moving[DOWN] == 1 and self.blocked[DOWN] == 0:
            self.y += PLAYER_SPEED

    def block_check(self):
        self.blocked = [0, 0, 0, 0]
        for i in self.game.mobs:
            self.contact_check(i)
        if self.x <= 0: self.blocked[LEFT] = 1
        if self.y <= 0: self.blocked[UP] = 1
        if self.x > SCREEN_WIDTH - 75:  self.blocked[RIGHT] = 1
        if self.y > SCREEN_HEIGHT - 116: self.blocked[DOWN] = 1

    def contact_check(self, obj):
        pass

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def render_ui(self, screen):
        screen.blit(self.toolbar_pack[0], (950, 15))
        m = 1
        z = self.hp // 2