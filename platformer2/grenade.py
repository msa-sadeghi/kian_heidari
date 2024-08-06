from pygame.sprite import Sprite
import pygame
from explosion import Explosion
class Grenade(Sprite):
    def __init__(self, x,y , direction):
        super().__init__()
        self.image = pygame.image.load("assets/icons/grenade.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
        self.speed = 7
        self.vel_y = -11
        self.timer = 100
        
    def update(self, explosion_group):
        self.vel_y += 1
        dx = self.direction * self.speed
        dy = self.vel_y
        if self.rect.y + dy > 300:
            dy = 0
            dx = 0
            
        if self.rect.right <= 0 or self.rect.left>= 800:
            self.direction *= -1 
            dx = self.direction * self.speed   
            
        self.rect.x += dx
        self.rect.y += dy
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(self.rect.centerx, self.rect.centery, explosion_group)
            # TODO REDUCE TARGET HEALTH( if grenade touches the enemy => reduce enemy health
            # otherwise reduce player's health)
            
            