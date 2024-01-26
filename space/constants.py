import pygame
SCREEN = pygame.display.set_mode()
SCREEN_WIDTH = SCREEN.get_width()
SCREEN_HEIGHT = SCREEN.get_height()
FPS = 60
CLOCK = pygame.time.Clock()
player_image = pygame.image.load("assets/spaceship.png")
enemy_image = pygame.image.load("assets/enemy.png")