from pygame.sprite import Sprite
import pygame
class ItemBox(Sprite):
    def __init__(self, item_type, x,y, item_box):
        super().__init__()
        self.item_type = item_type
        self.image = item_box[item_type]
        self.rect = self.image.get_rect()
        self.rect.midtop = (x + 50 // 2, y + 50 // 2)
        
    def update(self, player):
        if pygame.sprite.collide_rect(self, player):
            if self.item_type == "Health":
                player.health += 25
            elif self.item_type == "Ammo":
                player.ammo += 15
            elif self.item_type == "Grenade":
                player.grenade += 3
            self.kill()