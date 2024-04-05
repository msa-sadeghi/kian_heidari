import pygame

screen_width = 1065
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
FPS = 60
clock = pygame.time.Clock()

armour_img = pygame.image.load("assets/armour.png")
bg_img = pygame.image.load("assets/bg.png")
bullet_img = pygame.image.load("assets/bullet.png")
crosshair_img = pygame.image.load("assets/crosshair.png")
repair_img = pygame.image.load("assets/repair.png")

castle_25 = pygame.image.load("assets/castle/castle_25.png")
castle_50 = pygame.image.load("assets/castle/castle_50.png")
castle_100 = pygame.image.load("assets/castle/castle_100.png")
castle_images = [castle_100, castle_50, castle_25]

all_animation_images = []
all_enemy_types = ("knight", "goblin", "purple_goblin", "red_goblin")
all_enemy_healths = (75, 100, 125, 150)
all_animation_types = ("walk", "attack", "death")

for enemy in all_enemy_types:
    enemy_animation_list = []
    for animation in all_animation_types:
        animation_images = []
        for i in range(20):
            
            img = pygame.transform.scale(pygame.image.load(f"assets/enemies/{enemy}/{animation}/{i}.png"), (64,64))
            animation_images.append(img)
        enemy_animation_list.append(animation_images)
    all_animation_images.append(enemy_animation_list)
        
        