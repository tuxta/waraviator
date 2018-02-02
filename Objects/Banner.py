from GameFrame import RoomObject
import pygame


class Banner(RoomObject):
    def __init__(self, room, x, y):
        super().__init__(room, x, y)

        self.image = pygame.image.load("Images/banner.png")
        self.width = 600
        self.height = 44
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.depth = 100
