from constants import *
from world import World
from castle import Castle
from enemy import Enemy
import random
pygame.init()
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
    print(next_level)       
    game_world.draw() 
    if next_level:
        
        draw_text("Welcome to new Level",font, screen_width/2, screen_height/2)
        if pygame.time.get_ticks() - next_level_time > 2000:
            next_level_time = pygame.time.get_ticks()
            level_difficulty = 0
            MAX_difficulty *= 1.2
            enemy_group.empty()
            next_level = False
            last_spawn_time = pygame.time.get_ticks()
    castle.shoot(bullet_group) 
    castle.draw(screen)
    bullet_group.update()     
    bullet_group.draw(screen)     
    enemy_group.update(castle, bullet_group)     
    enemy_group.draw(screen)     
    pygame.display.update()
    clock.tick(FPS)