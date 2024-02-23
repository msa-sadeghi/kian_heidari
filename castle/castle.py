import pygame
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
        self.max_health = self.health
        self.alive = True
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        