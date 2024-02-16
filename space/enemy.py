from pygame.sprite import Sprite
from constants import *
from enemy_bullet import EnemyBullet
import random
class Enemy(Sprite):
    def __init__(self, image, x,y, bullet_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.speed = 4
        self.bullet_group = bullet_group
        

    def update(self):
        self.rect.x += self.direction * self.speed
        self.fire()
        
    def fire(self):
        if random.randint(1,3000) > 2999:
            EnemyBullet(self.rect.centerx, self.rect.bottom, self.bullet_group)
            
            
        
        
