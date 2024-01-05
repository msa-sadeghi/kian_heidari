from constants import *
from player import Player
from game import Game
pygame.init()


my_player = Player()

monster_group = pygame.sprite.Group()

my_game = Game(my_player, monster_group)
my_game.start_new_level()

start_time = pygame.time.get_ticks()

font72 = pygame.font.Font("assets/Abrushow.ttf", 72)
welcome_text = font72.render("Welcome to monster game", True, (50,120,190))
welcome_rect = welcome_text.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    SCREEN.fill((0,0,0))
    if pygame.time.get_ticks() - start_time < 2000:
        SCREEN.blit(welcome_text, welcome_rect)

    else:
        my_game.draw()
        my_player.move()
        my_player.draw()
        monster_group.draw(SCREEN)
        monster_group.update()

    pygame.display.update()
    CLOCK.tick(FPS)
