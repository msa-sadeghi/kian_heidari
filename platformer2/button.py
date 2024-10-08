import pygame

class Button:
    def __init__(self, x,y, image, scale) -> None:
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.release = True
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def if_clicked(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.release:
                action = True
                self.release = False
        if not pygame.mouse.get_pressed()[0]:
            self.release = True
                
        return action