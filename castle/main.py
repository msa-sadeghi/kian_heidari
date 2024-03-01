from constants import *
from world import World
from castle import Castle

game_world = World()
bullet_group = pygame.sprite.Group()
castle = Castle(castle_images, screen_width - 280,\
    screen_height- 350, 0.2)


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
    pygame.display.update()
    clock.tick(FPS)