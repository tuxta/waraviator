import pygame
import random
from GameFrame import Globals
from GameFrame import RoomObject


class Enemy(RoomObject):

    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = pygame.image.load("Images/enemy.png")
        self.width = 32
        self.height = 31
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.y_speed = 5
        self.depth = 50

        # - Accept collisions with the Plane - #
        # self.register_collision_object('Bullet')

    def step(self):
        if self.y >= Globals.SCREEN_HEIGHT:
            self.y = 0 - self.height*2
            self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)
