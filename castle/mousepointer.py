from constants import crosshair_img, pygame
class MousePointer:
    def __init__(self):
        self.image = pygame.transform.scale(crosshair_img, (40, 40))
        pygame.mouse.set_visible(False)
    def draw(self, screen):
        screen.blit(self.image, pygame.mouse.get_pos())