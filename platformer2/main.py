import pygame
from person import Person
from grenade import Grenade
from itembox import ItemBox
from healthbar import HealthBar
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
player = Person("player", 200, 200, 10, 5)
enemy = Person("enemy", 400, 200, 5, 0)
enemy_group.add(enemy)
moving_left=moving_right = False
shoot = False

health_box_img = pygame.image.load("assets/icons/health_box.png")
grenade_box_img = pygame.image.load("assets/icons/grenade_box.png")
ammo_box_img = pygame.image.load("assets/icons/ammo_box.png")

item_box_images = {
    'Health' : health_box_img,
    'Ammo' : ammo_box_img,
    'Grenade' : grenade_box_img
}
item_box_group = pygame.sprite.Group()
item_box = ItemBox('Health', 100, 260, item_box_images)
item_box_group.add(item_box)
item_box = ItemBox('Ammo', 400, 260, item_box_images)
item_box_group.add(item_box)
item_box = ItemBox('Grenade', 500, 260, item_box_images)
item_box_group.add(item_box)

health_bar = HealthBar(10, 10, player.health, player.max_health)

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
                
    if player.alive:        
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
    print(player.action)    
    screen.fill((0,0,0))       
    player.draw(screen)
    enemy.draw(screen)
    player.update()
    enemy.update()
    enemy.move(False, False)
    bullet_group.update(player, enemy, bullet_group)
    bullet_group.draw(screen)
    enemy_bullet_group.update(player, enemy, enemy_bullet_group)
    enemy_bullet_group.draw(screen)
    grenade_group.update(explosion_group, player, enemy_group)
    grenade_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    for enemy in enemy_group:
        enemy.ai(player, enemy_bullet_group)
    enemy_group.update()
    enemy_group.draw(screen)
    item_box_group.update(player)
    item_box_group.draw(screen)
    health_bar.draw(player.health, screen)
    pygame.display.update()
    clock.tick(FPS)
    