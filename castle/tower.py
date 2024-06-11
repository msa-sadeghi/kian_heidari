import pygame
import math
from bullet import Bullet
from constants import bullet_img
from pygame.sprite import Sprite
class Tower(Sprite):
    def __init__(self, images, x,y, scale):
        super().__init__()
        self.image100 = pygame.transform.scale(images[0],\
             (scale * images[0].get_width(),\
                 scale * images[0].get_height()))
        self.image50 = pygame.transform.scale(images[1],\
             (scale * images[1].get_width(),\
                 scale * images[1].get_height()))
        self.image25 = pygame.transform.scale(images[2],\
             (scale * images[2].get_width(),\
                 scale * images[2].get_height()))
        
        self.image = self.image100
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.last_bullet_spawn_time = pygame.time.get_ticks()

    def update(self, enemy_group, bullet_group, castle):
        self.got_target = False
        for enemy in enemy_group:
            if enemy.alive:
                target_x, target_y = enemy.rect.midbottom
                self.got_target = True
                break
        if self.got_target:
            x_dist = target_x - self.rect.midleft[0]
            y_dist = -(target_y - self.rect.midleft[1])
            self.angle = math.atan2(y_dist, x_dist)
            if pygame.time.get_ticks() - self.last_bullet_spawn_time> 1000:
                self.last_bullet_spawn_time = pygame.time.get_ticks()
                bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
                bullet_group.add(bullet)
            
        if castle.health <= 250:
            self.image = self.image25
        elif castle.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100
     
            
            
                
            
            
        
   