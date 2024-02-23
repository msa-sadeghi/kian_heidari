from constants import bg_img, screen

class World:
    def __init__(self):
        self.image = bg_img
        self.rect = self.image.get_rect(topleft=(0,0))
        
    def draw(self):
        screen.blit(self.image, self.rect)