import pygame
from person import Person
from grenade import Grenade
from itembox import ItemBox
from healthbar import HealthBar 
import csv

from world import World
pygame.init()

ROWS = 16
MAX_COLS = 150
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
FPS = 60
TILE_SIZE = SCREEN_HEIGHT // ROWS
scroll = 0
screen_scroll = 0
TILE_TYPES = 21
level = 1
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
grenade_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
# player = Person("player", 200, 200, 10, 5)
# enemy = Person("enemy", 400, 200, 5, 0)
# enemy_group.add(enemy)
moving_left=moving_right = False
shoot = False

pine1_img = pygame.image.load("assets/background/pine1.png")
pine2_img = pygame.image.load("assets/background/pine2.png")
mountain_img = pygame.image.load("assets/background/mountain.png")
sky_img = pygame.image.load("assets/background/sky_cloud.png")

img_list = []
for i in range(TILE_TYPES):
    img = pygame.image.load(f"assets/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)



def draw_bg():
    screen.fill((0,255,0))
    width = sky_img.get_width()
    for i in range(4):
        screen.blit(sky_img, (i * width - scroll * 0.5 ,0))
        screen.blit(mountain_img, (i * width - scroll * 0.6,SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, (i * width - scroll * 0.7,SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, (i * width - scroll * 0.8,SCREEN_HEIGHT - pine2_img.get_height() ))    



health_box_img = pygame.image.load("assets/icons/health_box.png")
grenade_box_img = pygame.image.load("assets/icons/grenade_box.png")
ammo_box_img = pygame.image.load("assets/icons/ammo_box.png")

item_box_images = {
    'Health' : health_box_img,
    'Ammo' : ammo_box_img,
    'Grenade' : grenade_box_img
}
world_data = []

for row in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)



with open(f"level{level}.csv", newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for j, row in enumerate(reader):
        for i, tile in enumerate(row):
            world_data[j][i] = int(tile)


item_box_group = pygame.sprite.Group()
world = World()
player , health_bar = world.process_data(world_data, img_list, TILE_SIZE,
                                         item_box_group,item_box_images,enemy_group)




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
        screen_scroll = player.move(moving_left, moving_right, world,scroll)
        print(scroll)
        scroll -= screen_scroll
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
    draw_bg()       
    player.draw(screen)
    # enemy.draw(screen)
    player.update()
    # enemy.update()
    # enemy.move(False, False)
    for enemy in enemy_group:
        bullet_group.update(player, enemy, bullet_group)
        enemy_bullet_group.update(player, enemy, enemy_bullet_group)
    bullet_group.draw(screen)
    enemy_bullet_group.draw(screen)
    grenade_group.update(explosion_group, player, enemy_group)
    grenade_group.draw(screen)
    explosion_group.update()
    explosion_group.draw(screen)
    for enemy in enemy_group:
        enemy.ai(player, enemy_bullet_group, world,scroll)
        enemy.update()
        enemy.draw(screen)
    
    item_box_group.update(player)
    item_box_group.draw(screen)
    health_bar.draw(player.health, screen)
    world.draw(screen, screen_scroll)
    pygame.display.update()
    clock.tick(FPS)
    
    