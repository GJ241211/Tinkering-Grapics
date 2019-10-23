### imports

import pygame

pygame.init()

### variables

tile_width = 32
tile_height = 32

window_width = 640
window_height = 480

map_width  = 640
map_height = 440
map_gap    = int(1/4*map_width)

tiles_x = int(map_width/tile_width)
tiles_y = int(map_height/tile_height/3*4)


### Colours
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

### desert
DARK_ORANGE = (160, 75,  0)
DARK_YELLOW = (180,140,  0)
ORANGE      = (225,110,  0)
YELLOW      = (240,240, 50)

### forrest
TREE_GREEN  = ( 90,160, 40)
GRASS_GREEN = ( 90,225, 40)
TREE_BROWN  = ( 90, 60,  0)
DARK_GREY   = (100,100,100)

### ice
DARK_BLUE   = (  0,  0,140)
LIGHT_BLUE  = ( 75,240,255)
LIGHT_GREY  = (205,205,205)
# WHITE #

### fire
RED         = (200,  0,  0)
DARK_RED    = (140,  0,  0)
# ORANGE #
# YELLOW #

### clouds
LIGHT_YELLOW = (240,240,140)
# dark_grey #
# white #
# light_grey #

### terrains

TERR_DESERT  = (DARK_ORANGE,DARK_YELLOW,ORANGE,YELLOW)
TERR_FORREST = (TREE_GREEN,TREE_BROWN,GRASS_GREEN,DARK_GREY)
TERR_ICE     = (DARK_BLUE,LIGHT_BLUE,LIGHT_GREY,WHITE)
TERR_FIRE    = (DARK_RED,RED,ORANGE,YELLOW)
TERR_CLOUDS  = (DARK_GREY,LIGHT_YELLOW,LIGHT_GREY,WHITE)

### creating tiles


# basic tile
def basic_tile(terrain, tile_x, tile_y):
    global tile
    tile = pygame.draw.rect(display_surf, DARK_ORANGE, (0, 200, tile_width, tile_height))


# pillar tile
def pillar_tile(terrain):
    global tile
    tile = pygame.draw.rect(display_surf, RED, (0, 200, tile_width, tile_height))


# bridge tile
def bridge_tile(terrain):
    global tile
    tile = pygame.draw.rect(display_surf, YELLOW, (0, 200, tile_width, tile_height))

### set up
display_surf = pygame.display.set_mode((window_width, window_height))
display_surf.fill(WHITE)
tile = pygame.draw.rect(display_surf, BLACK, (0,200,tile_width,tile_height))
pygame.display.set_caption('Tiles')

map = []
for x in range(tiles_x): # x is a row and y is a column
    # Add an empty array that will hold each cell
    map.append([])
    for y in range(tiles_y):
        map[x].append(0)


### deffinitions

### gameloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for x in range(0,tile_width):
        column = []
        for y in range((0 + map_gap), (tile_height + map_gap)):
            column.append(basic_tile(TERR_CLOUDS, x, y))
            map.append(column)

    pygame.display.update()
