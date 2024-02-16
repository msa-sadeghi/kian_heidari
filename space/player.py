from pygame.sprite import Sprite
from constants import *
from player_bullet import PlayerBullet
class Player(Sprite):
    def __init__(self, image, bullet_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCREEN_HEIGHT
        self.rect.centerx = SCREEN_WIDTH/2
        self.speed = 7
        self.lives = 3
        self.bullet_group = bullet_group

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
            
    def fire(self):
        PlayerBullet(self.rect.centerx, self.rect.top, self.bullet_group)
        