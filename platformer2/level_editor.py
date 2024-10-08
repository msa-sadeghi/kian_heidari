import pygame
import pickle
from button import Button
pygame.init()
clock = pygame.time.Clock()
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
LOWER_MARGIN = 100
SIDE_MARGIN = 300

ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS

TILE_TYPES = 21

current_tile = 0

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

level = 0

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

def draw_grid():
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, (255,255,255), (i * TILE_SIZE - scroll , 0), (i * TILE_SIZE - scroll , SCREEN_HEIGHT))
        
    for j in range(ROWS + 1):
        pygame.draw.line(screen, (255,255,255), (0, j * TILE_SIZE), (SCREEN_WIDTH, j * TILE_SIZE))
    
img_list = []
for i in range(TILE_TYPES):
    img = pygame.image.load(f"assets/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    img_list.append(img)


button_list = []
row = 0
col = 0
for i in range(len(img_list)):
    tile_button = Button(SCREEN_WIDTH + 75 * col + 50, 75 * row + 50,img_list[i], 1)
    button_list.append(tile_button)
    col += 1
    if col == 3:
        row += 1
        col = 0

world_data = []

for row in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

for tile in range(MAX_COLS)   :
    world_data[ROWS - 1][tile] = 0

def draw_world(): 
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] >= 0:
                screen.blit(img_list[world_data[i][j]], (j * TILE_SIZE - scroll, i * TILE_SIZE))
    



current_tile = 0
running = True
while running:
    
    if scroll_left and scroll>0:
        scroll -= 5 * scroll_speed
    if scroll_right and scroll < (MAX_COLS * TILE_SIZE) - SCREEN_WIDTH:
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
    draw_grid()
    draw_world()
    pygame.draw.rect(screen, (0,255, 0), (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))
    
    for i in range(len(button_list)):
        button_list[i].draw(screen)
        if button_list[i].if_clicked():
            current_tile = i
            
    mouse_pos = pygame.mouse.get_pos()
    x = (mouse_pos[0] + scroll)//TILE_SIZE
    y = mouse_pos[1]//TILE_SIZE
    if mouse_pos[0] < SCREEN_WIDTH and mouse_pos[1] < SCREEN_HEIGHT:
        if pygame.mouse.get_pressed()[0]:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        elif pygame.mouse.get_pressed()[2]:
            world_data[y][x] = -1
    
    
    pygame.draw.rect(screen, (255, 0,0), button_list[current_tile].rect, 3)
    pygame.display.update()
    clock.tick(FPS)