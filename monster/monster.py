from pygame.sprite import Sprite
import random
from constants import *
class Monster(Sprite):
    def __init__(self,image,type,x,y, monster_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.type = type
        self.speed = random.randint(1,5)
        self.dx = random.choice((-1,1))
        self.dy = random.choice((-1,1))
        monster_group.add(self)


    def update(self):

        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed

        if self.rect.left <=0 or self.rect.right >= SCREEN_WIDTH:
            self.dx *= -1

        if self.rect.top <= 100 or self.rect.bottom >= SCREEN_HEIGHT - 100:
            self.dy *= -1


