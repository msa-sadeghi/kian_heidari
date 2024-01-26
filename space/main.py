from constants import *
from player import Player
from enemy import Enemy
pygame.init()
player = Player(player_image)
enemy_group = pygame.sprite.Group()

level = 0
def start_new_level():
    global level
    level += 1
    for i in range(5):
        for j in range(15):
            enemy_group.add(Enemy(enemy_image, j * 96, i * 96))



start_new_level()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    SCREEN.fill((0,0,0))
    player.move()
    player.draw()
    enemy_group.update()
    enemy_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)
