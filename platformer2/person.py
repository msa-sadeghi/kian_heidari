from pygame.sprite import Sprite
import os
import pygame
from bullet import Bullet
class Person(Sprite):
    def __init__(self,char_type, x,y, ammo, grenade):
        super().__init__()
        animation_types = ("Idle", "Run", "Jump", "Death")
        self.animation_list = []
        self.char_type = char_type
        for animation in animation_types:
            t = []
            n_images = len(os.listdir(f"assets/{self.char_type}/{animation}"))
            for i in range(n_images):
                img = pygame.image.load(f"assets/{self.char_type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                t.append(img)
            self.animation_list.append(t) 
        self.image = self.animation_list[0][0]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.image_number = 0
        self.action = 0
        self.speed = 5
        self.last_update_time = 0
        self.flip = False
        self.direction = 1
        self.last_shoot_time = 0
        self.ammo = ammo
        self.grenade = grenade
        self.health = 100
        self.max_health = 100
        self.vel_y = 0
        self.jump = False
        self.in_air = False
        
    def update(self):
        self.animation()
        
    def shoot(self, group):
        if pygame.time.get_ticks() - self.last_shoot_time > 200 and self.ammo > 0:
            self.last_shoot_time = pygame.time.get_ticks()
            self.ammo -= 1
            Bullet(self.rect.centerx + 0.6 * self.rect.size[0] * self.direction, \
                self.rect.centery, self.direction, group)
            
  
            
    
    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image,self.flip, False ), self.rect)
        
    def animation(self):
        self.image = self.animation_list[self.action][self.image_number]
        if pygame.time.get_ticks() - self.last_update_time > 100:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.animation_list[self.action]):
                if self.action == 3:
                    self.image_number = len(self.animation_list[self.action]) -1
                else:
                    self.image_number = 0
    
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0
    
    def move(self, moving_left, moving_right):
        dx = dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if self.jump == True:
            self.vel_y = -11
            self.in_air = True
        self.vel_y += 1     
        dy += self.vel_y
        if self.rect.bottom + dy > 300:
            dy = 0
            self.in_air = False
        self.rect.x += dx
        self.rect.y += dy
            