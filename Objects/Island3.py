import pygame
import random
from GameFrame import Globals
from GameFrame import RoomObject


class Island3(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = pygame.image.load("Images/island3.png")
        self.width = 64
        self.height = 65
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.y_speed = 4
        self.depth = -100

    def step(self):
        if self.y >= Globals.SCREEN_HEIGHT:
            self.y = 0 - self.height*2
            self.x = random.randint(0, Globals.SCREEN_WIDTH - self.width)
