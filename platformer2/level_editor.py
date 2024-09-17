import pygame
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1



screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pine1_img = pygame.image.load("assets/background/pine1.png")
pine2_img = pygame.image.load("assets/background/pine2.png")
mountain_img = pygame.image.load("assets/background/mountain.png")
sky_img = pygame.image.load("assets/background/sky_cloud.png")
def draw_bg():
    screen.fill((0,255,0))
    width = sky_img.get_width()
    for i in range(4):
        screen.blit(sky_img, (i * width - scroll * 0.5 ,0))
        screen.blit(mountain_img, (i * width - scroll * 0.6,SCREEN_HEIGHT - mountain_img.get_height() - 300))
        screen.blit(pine1_img, (i * width - scroll * 0.7,SCREEN_HEIGHT - pine1_img.get_height() - 150))
        screen.blit(pine2_img, (i * width - scroll * 0.8,SCREEN_HEIGHT - pine2_img.get_height() ))    
running = True
while running:
    
    if scroll_left and scroll>0:
        scroll -= 5 * scroll_speed
    if scroll_right:
        scroll += 5 * scroll_speed
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_RSHIFT:
                scroll_speed = 1
    draw_bg()
    pygame.display.update()
    clock.tick(FPS)