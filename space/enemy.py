from pygame.sprite import Sprite
from constants import *

class Enemy(Sprite):
    def __init__(self, image, x,y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.speed = 4
        

    def update(self):
        self.rect.x += self.direction * self.speed
