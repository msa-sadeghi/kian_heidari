from constants import *
from world import World
from castle import Castle
from enemy import Enemy
from button import Button
from mousepointer import MousePointer
import random
pygame.init()


def show_text(txt, color, font, position):
    text = font.render(txt, True, color)
    rect = text.get_rect(topleft=position)
    screen.blit(text, rect)


font32 = pygame.font.SysFont("arial", 32)
level = 1
repair_btn = Button(pygame.transform.scale(repair_img, (40,40)), screen_width - 50, 10)
armour_btn = Button(pygame.transform.scale(armour_img, (40,40)), screen_width - 100, 10)
mouse = MousePointer()
game_world = World()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
castle = Castle(castle_images, screen_width - 280,\
    screen_height- 350, 0.2)

next_level_time = pygame.time.get_ticks()
font = pygame.font.Font("assets/Abrushow.ttf", 48)
def draw_text(text, font, x,y):
    t = font.render(text, True, (120,10,190))
    r = t.get_rect(center=(x,y))
    screen.blit(t,r)


MAX_difficulty = 100
level_difficulty = 0
next_level = False
last_spawn_time = pygame.time.get_ticks()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if level_difficulty < MAX_difficulty:
        if pygame.time.get_ticks() - last_spawn_time > 2000:
            last_spawn_time = pygame.time.get_ticks()
            j = random.randrange(len(all_enemy_types))
            enemy = Enemy(all_enemy_healths[j], all_animation_images[j], -50, 300, 1)
            enemy_group.add(enemy)
            level_difficulty += all_enemy_healths[j]
    if level_difficulty >= MAX_difficulty:
        enemies = 0
        for enemy in enemy_group:
            if enemy.alive :
                enemies += 1
        if enemies == 0 and not next_level :
            next_level = True
            next_level_time = pygame.time.get_ticks()
    game_world.draw() 
    if next_level:
        
        draw_text("Welcome to new Level",font, screen_width/2, screen_height/2)
        if pygame.time.get_ticks() - next_level_time > 2000:
            next_level_time = pygame.time.get_ticks()
            level_difficulty = 0
            MAX_difficulty *= 1.2
            enemy_group.empty()
            next_level = False
            level += 1
            last_spawn_time = pygame.time.get_ticks()
    
    mouse.draw(screen)
    r = repair_btn.draw(screen)
    
    if r:
        castle.repair()
    r = armour_btn.draw(screen)
    
    if r:
        castle.armour()
    show_text(f"Level: {level}", (240,10,123), font32, (10,10))
    show_text(f"Health: {castle.health}", (240,10,123), font32, (390,10))
    show_text(f"MaxHealth: {castle.max_health}", (240,10,123), font32, (10,50))
    show_text(f"money: {castle.money}", (240,10,123), font32, (390,50))
    
    castle.shoot(bullet_group) 
    castle.draw(screen)
    bullet_group.update()     
    bullet_group.draw(screen)     
    enemy_group.update(castle, bullet_group)     
    enemy_group.draw(screen)     
    pygame.display.update()
    clock.tick(FPS)