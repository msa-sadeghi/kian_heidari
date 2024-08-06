from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.image = pygame.image.load("assets/icons/bullet.png")
        self.rect = self.image.get_rect(center=(x,y))
        self.direction = direction
        self.speed = 4
        group.add(self)
        
    def update(self, player,enemy , bullet_group):
        self.rect.x += self.direction * self.speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.kill()      
        if pygame.sprite.spritecollide(player, bullet_group, True):
            player.health -= 20
            if player.health < 0:
                player.health = 0
                player.update_action(3)
        if pygame.sprite.spritecollide(enemy, bullet_group, True):
            enemy.health -= 20
            if enemy.health < 0:
                enemy.health = 0
                enemy.update_action(3)