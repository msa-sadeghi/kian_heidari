import pygame
import math
from bullet import Bullet
from constants import bullet_img
class Castle:
    def __init__(self, images, x,y, scale):
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
        
        self.health = 1000
        self.money = 0
        self.score = 0
        self.max_health = self.health
        self.alive = True
        self.clicked = False
        
    def draw(self, screen):
        if self.health <= 250:
            self.image = self.image25
        elif self.health <= 500:
            self.image = self.image50
        else:
            self.image = self.image100
        screen.blit(self.image, self.rect)
        
    def shoot(self, bullet_group):
        mouse_pos = pygame.mouse.get_pos()
        y_distance = -(mouse_pos[1] - self.rect.midleft[1])
        x_distance = mouse_pos[0] - self.rect.midleft[0]
        self.angle = math.atan2(y_distance, x_distance)
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            bullet = Bullet(bullet_img, self.rect.midleft[0], self.rect.midleft[1], self.angle)
            bullet_group.add(bullet)
            self.clicked = True
        if not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            
            
        
        