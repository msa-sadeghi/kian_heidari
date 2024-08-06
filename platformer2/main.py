import pygame
from person import Person
from grenade import Grenade
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
player = Person("player", 200, 200, 10, 5)
enemy = Person("enemy", 400, 200, 5, 0)
moving_left=moving_right = False
shoot = False

grenade = False
grenade_rel = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                player.jump = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_g:
                grenade = True
                grenade_rel = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                player.jump = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade = False
                grenade_rel = False
                
    player.move(moving_left, moving_right)
            
    if moving_left or moving_right:
        player.update_action(1)
    elif player.in_air:
        player.update_action(2)
    else:
        player.update_action(0)
        
    if shoot:
        player.shoot(bullet_group)
    elif grenade and player.grenade > 0 and grenade_rel:
        grenade_rel = False
        g = Grenade(player.rect.centerx + player.rect.size[0]/2, player.rect.top, player.direction)
        grenade_group.add(g)
        player.grenade -= 1
        
    screen.fill((0,0,0))       
    player.draw(screen)
    enemy.draw(screen)
    player.update()
    enemy.update()
    enemy.move(False, False)
    bullet_group.update(player, enemy, bullet_group)
    bullet_group.draw(screen)
    grenade_group.update(explosion_group)
    grenade_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    