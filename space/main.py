from constants import *
from player import Player
from enemy import Enemy
pygame.init()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()

player = Player(player_image,player_bullet_group)
enemy_group = pygame.sprite.Group()

level = 0
score = 0
def start_new_level():
    global level
    level += 1
    for i in range(5):
        for j in range(15):
            enemy_group.add(Enemy(enemy_image, j * 96, i * 96, enemy_bullet_group))



start_new_level()

font = pygame.font.SysFont("Arial", 32)

def game_over():
    print("game over")
    global running, level, score
    level = 0
    game_over_text = font.render("Game Over", True, (231, 18,190))
    game_over_rect = game_over_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    SCREEN.fill((0,0,0))
    SCREEN.blit(game_over_text, game_over_rect)
    pygame.display.update()
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
                    running = False
                if event.key == pygame.K_RETURN:
                    paused = False
                    score = 0
                    player.lives = 3
                    enemy_group.empty()
                    start_new_level()


def check_if_on_edge():
    on_edge = False
    for enemy in enemy_group:
        if enemy.rect.left < 0 or enemy.rect.right > SCREEN_WIDTH:
            on_edge = True
            break
    if on_edge:
        breach = False
        for enemy in enemy_group:
            enemy.direction *= -1
            enemy.rect.y += level * 25
            
            if enemy.rect.bottom >= SCREEN_HEIGHT - 100:
                breach = True
        if breach == True:
            game_over()


def check_collisions():
    if pygame.sprite.groupcollide(player_bullet_group, enemy_group, True, True):
        pass
    if pygame.sprite.groupcollide(player_bullet_group, enemy_bullet_group, True, True):
        pass
    if pygame.sprite.spritecollide(player, enemy_bullet_group, True):
        pass
    



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
            if event.key == pygame.K_SPACE:
                player.fire()
    check_collisions()
    
    SCREEN.fill((0,0,0))
    check_if_on_edge()
    player.move()
    player.draw()
    enemy_group.update()
    enemy_group.draw(SCREEN)
    player_bullet_group.update()
    player_bullet_group.draw(SCREEN)
    enemy_bullet_group.update()
    enemy_bullet_group.draw(SCREEN)
    pygame.display.update()
    CLOCK.tick(FPS)
