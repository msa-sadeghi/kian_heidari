import pygame
from person import Person
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Person("player", 200, 200)
enemy = Person("enemy", 400, 200)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))       
    player.draw(screen)
    enemy.draw(screen)
    player.update()
    enemy.update()
    pygame.display.update()
    clock.tick(FPS)
    