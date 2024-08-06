from pygame.sprite import Sprite
import pygame
class Explosion(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.images = []
        for i in range(1, 6):
            img = pygame.image.load(f"assets/explosion/exp{i}.png")
            self.images.append(img)
            
        self.image = self.images[0]
        self.image_number = 0
        self.rect = self.image.get_rect(center=(x,y))
        self.time = 0
        group.add(self)
        
    def update(self)   :
        if pygame.time.get_ticks() - self.time > 100:
            self.image_number += 1
            self.time = pygame.time.get_ticks()
            if self.image_number >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.image_number]
                
 