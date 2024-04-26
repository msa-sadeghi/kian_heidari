from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, health, animation_list, x,y, speed):
        super().__init__()
        self.alive = True
        self.speed = speed
        self.health = health
        self.animation_type_number = 0# 0 > walk   1 > attack   2 > death
        self.frame_index = 0
        self.animation_list = animation_list
        self.image = self.animation_list[self.animation_type_number][self.frame_index]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.last_animation_time = pygame.time.get_ticks()
        self.last_attack_time = pygame.time.get_ticks()
    def update(self, target, bullet_group):
        if self.alive:
            if self.rect.right > target.rect.left:
                self.update_action(1)
            if self.animation_type_number == 0:
                self.rect.x += self.speed 
            if self.animation_type_number == 1:
                if pygame.time.get_ticks() - self.last_attack_time > 1000:
                    self.last_attack_time = pygame.time.get_ticks()
                    target.health -= 100
                    if target.health < 0:
                        target.health = 0
            
            if pygame.sprite.spritecollide(self, bullet_group, True):
                self.health -= 25
            if self.health <= 0:
                self.alive = False
                target.money += 200
                target.score += 50
                self.update_action(2)
                
            
        self.update_animation() 
    
    def update_action(self, new_action)    :
        if self.animation_type_number != new_action:
            self.animation_type_number = new_action
            self.frame_index = 0
            self.last_animation_time = pygame.time.get_ticks()
        
             
    def update_animation(self):
        self.image = self.animation_list[self.animation_type_number][self.frame_index]
        if pygame.time.get_ticks() - self.last_animation_time > 50:
            self.last_animation_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.animation_type_number]):
            if self.animation_type_number == 2:
                self.frame_index = len(self.animation_list[self.animation_type_number]) - 1
            else:
                self.frame_index = 0
        
                
        