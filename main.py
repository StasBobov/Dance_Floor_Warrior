import pygame
import sys
from Constants import *
from Player import *
from Mob import Chick


class Main:

    def __init__(self, screen):
        self.screen = screen
        self.player = Player(game=self)
        self.background = pygame.image.load('Dance Floor.jpg')
        self.mobs = []
        self.running = True
        self.main_loop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.player.direction = RIGHT
                    self.player.moving = [1, 0, 0, 0]
                if event.key == pygame.K_DOWN:
                    self.player.direction = DOWN
                    self.player.moving = [0, 1, 0, 0]
                if event.key == pygame.K_LEFT:
                    self.player.direction = LEFT
                    self.player.moving = [0, 0, 1, 0]
                if event.key == pygame.K_UP:
                    self.player.direction = UP
                    self.player.moving = [0, 0, 0, 1]

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.moving[RIGHT] = 0
                if event.key == pygame.K_DOWN:
                    self.player.moving[DOWN] = 0
                if event.key == pygame.K_LEFT:
                    self.player.moving[LEFT] = 0
                if event.key == pygame.K_UP:
                    self.player.moving[UP] = 0

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.render(screen)
        self.player.render_ui(screen)
        for i in self.mobs:
            i.render(screen)
        pygame.display.flip()

    def move(self):
        self.player.move()

    def main_loop(self):
        self.add_npc()
        while self.running == True:
            self.move()
            self.render()
            self.handle_events()

    def add_npc(self):
        self.mobs.append(Chick(game=self))


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Dance Floor Warrior')
game = Main(screen)



# clock = pygame.time.Clock()

# pygame.display.update()

# while True:
#     clock.tick(30)

#     kees = pygame.key.get_pressed()
#
#     if kees[pygame.K_LEFT] and x > 5:
#         x -= speed
#     elif kees[pygame.K_RIGHT] and x < win_w - 75 - 5:
#         x += speed
#     elif kees[pygame.K_DOWN] and y < win_h - 116 - 5:
#         y += speed
#     elif kees[pygame.K_UP] and y > 5:
#         y -= speed


