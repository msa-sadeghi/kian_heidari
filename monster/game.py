import pygame.sprite

from constants import *
from monster import Monster
import random


class Game:
    def __init__(self, player, monster_group):
        self.player = player
        self.monster_group = monster_group

        self.score = 0
        self.level_number = 0

        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        yellow_monster = pygame.image.load("assets/yellow_monster.png")

        self.all_monster_images = (blue_monster, green_monster, purple_monster, yellow_monster)
        self.target_monster_type = random.randint(0, 3)
        self.target_monster_image = self.all_monster_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect(centerx=SCREEN_WIDTH / 2, bottom=100)
        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")
    def start_new_level(self):
        self.level_number += 1
        for i in range(self.level_number):
            Monster(self.all_monster_images[0], 0, random.randint(0, SCREEN_WIDTH - 64),
                    random.randint(100, SCREEN_HEIGHT - 100), self.monster_group)
            Monster(self.all_monster_images[1], 1, random.randint(0, SCREEN_WIDTH - 64),
                    random.randint(100, SCREEN_HEIGHT - 100), self.monster_group)
            Monster(self.all_monster_images[2], 2, random.randint(0, SCREEN_WIDTH - 64),
                    random.randint(100, SCREEN_HEIGHT - 100), self.monster_group)
            Monster(self.all_monster_images[3], 3, random.randint(0, SCREEN_WIDTH - 64),
                    random.randint(100, SCREEN_HEIGHT - 100), self.monster_group)

    
    def choose_new_target(self):
        new_target = random.choice(self.monster_group.sprites())
        self.target_monster_image = new_target.image
        self.target_monster_type = new_target.type
    
    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                collided_monster.remove(self.monster_group)
                self.catch_sound.play()
                if len(self.monster_group) == 0:
                    self.start_new_level()
                else:
                    self.choose_new_target()
            else:
                self.die_sound.play()
                self.player.reset()

    def draw(self):
        COLORS = (
            (8, 175, 237),
            (111, 214, 33),
            (236, 69, 253),
            (245, 167, 22)

        )
        SCREEN.blit(self.target_monster_image, self.target_monster_rect)
        pygame.draw.rect(SCREEN, COLORS[self.target_monster_type], (0, 100, SCREEN_WIDTH, SCREEN_HEIGHT - 200), 4)
