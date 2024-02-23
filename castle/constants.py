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