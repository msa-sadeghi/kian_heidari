import math
from constants import screen_width,screen_height, pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    def __init__(self, image, x,y,angle):
        super().__init__()
        self.image = pygame.transform.scale(image, (image.get_width() * .2, image.get_height() * .2))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.angle = angle
        self.speed = 10
        self.dx = math.cos(self.angle) * self.speed
        self.dy = -math.sin(self.angle) * self.speed
        
    def update(self):
        if self.rect.right < 0 or self.rect.left > screen_width\
            or self.rect.top > screen_height or self.rect.bottom < 0:
                self.kill()
                
        self.rect.x += self.dx
        self.rect.y += self.dy
            
        