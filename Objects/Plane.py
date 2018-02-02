import pygame
from GameFrame import Globals
from GameFrame import RoomObject
from Objects.Bullet import Bullet


class Plane(RoomObject):
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        self.image = pygame.image.load("Images/plane.png")
        self.width = 59
        self.height = 42
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.depth = 100

        # - Register the Plane to handle key events - #
        self.handle_key_events = True

        # - Allow bullet fire (limit firing) - #
        self.can_shoot = True

        # - Register collisions with enemy - #
        self.register_collision_object('Enemy')

    def step(self):
        # - Keep object in the room - #
        if self.rect.left <= 0:
            self.x = 0
        elif self.rect.right >= Globals.SCREEN_WIDTH:
            self.x = Globals.SCREEN_WIDTH - self.width
        if self.rect.top <= 0:
            self.y = 0
        elif self.rect.bottom >= Globals.SCREEN_HEIGHT - 60:
            self.y = Globals.SCREEN_HEIGHT - 60 - self.height

    def key_pressed(self, key):
        if key[pygame.K_LEFT]:
            self.x -= 4
        if key[pygame.K_RIGHT]:
            self.x += 4
        if key[pygame.K_UP]:
            self.y -= 4
        if key[pygame.K_DOWN]:
            self.y += 4
        if key[pygame.K_SPACE]:
            self.fire_bullet()

    def fire_bullet(self):
        if self.can_shoot:
            self.room.fire_bullet_sound.play()
            new_bullet = Bullet(self.room, self.rect.centerx, self.y)
            new_bullet.x -= 4
            self.room.add_room_object(new_bullet)
            self.room.set_timer(15, self.reset_shooting)
            self.can_shoot = False

    def reset_shooting(self):
        self.can_shoot = True

    def handle_collision(self, other):
        print('Planes collide')
        other_type = type(other).__name__
        if other_type == 'Enemy':
            self.delete_object(other)
            self.room.update_score(-1)
            if Globals.LIVES <= 0:
                self.room.running = False
                self.room.quitting = True
