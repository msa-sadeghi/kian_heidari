from constants import *
from world import World
from castle import Castle
from enemy import Enemy
game_world = World()
bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
castle = Castle(castle_images, screen_width - 280,\
    screen_height- 350, 0.2)

e1 = Enemy(all_enemy_healths[0], all_animation_images[0], 100, screen_height - 250, 1)
enemy_group.add(e1)
e2 = Enemy(all_enemy_healths[1], all_animation_images[1], 100, screen_height - 200, 1)
enemy_group.add(e2)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw() 
    castle.shoot(bullet_group) 
    castle.draw(screen)
    bullet_group.update()     
    bullet_group.draw(screen)     
    enemy_group.update(castle, bullet_group)     
    enemy_group.draw(screen)     
    pygame.display.update()
    clock.tick(FPS)