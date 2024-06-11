from pygame.sprite import Sprite
import os
import pygame
class Person(Sprite):
    def __init__(self,char_type, x,y):
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
        
    def update(self):
        self.animation()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def animation(self):
        pass