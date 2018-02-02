import pygame
from GameFrame import RoomObject
from GameFrame import Globals


class Bullet(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = pygame.image.load("Images/bullet.png")
        self.width = 9
        self.height = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.y_speed = -8

        # Register for collision with Enemy plane
        self.register_collision_object('Enemy')

    def step(self):
        if self.y < 0 - self.height:
            self.room.delete_object(self)

    def handle_collision(self, other):
        other_type = type(other).__name__
        if other_type == 'Enemy':
            self.room.explosion_sound.play()
            Globals.destroyed_count += 1
            if Globals.destroyed_count >= 10:
                self.room.running = False
                Globals.total_count = 0
                Globals.destroyed_count = 0

            self.room.delete_object(other)
            self.room.delete_object(self)
