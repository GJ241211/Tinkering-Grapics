###imports

import pygame

pygame.init()

###variables

tile_height = 32
tile_width = 32

window_width = 640
window_height = 480

###Colours
BLACK = (  0,  0,  0)
WHITE = (255,255,255)

###desert
DARK_ORANGE = (160, 75,  0)
DARK_YELLOW = (180,140,  0)
ORANGE      = (225,110,  0)
YELLOW      = (240,240, 50)

###forrest
TREE_GREEN  = ( 90,160, 40)
GRASS_GREEN = ( 90,225, 40)
TREE_BROWN  = ( 90, 60,  0)
DARK_GREY   = (100,100,100)

###ice
DARK_BLUE   = (  0,  0,140)
LIGHT_BLUE  = ( 75,240,255)
LIGHT_GREY  = (205,205,205)
#WHITE#

###fire
RED         = (200,  0,  0)
DARK_RED    = (140,  0,  0)
#ORANGE#
#YELLOW#

###clouds
LIGHT_YELLOW = (240,240,140)
#dark_grey#
#white#
#light_grey#

###terrains

MAP_DESERT  = (DARK_ORANGE,DARK_YELLOW,ORANGE,YELLOW)
MAP_FORREST = (TREE_GREEN,TREE_BROWN,GRASS_GREEN,DARK_GREY)
MAP_ICE     = (DARK_BLUE,LIGHT_BLUE,LIGHT_GREY,WHITE)
MAP_FIRE    = (DARK_RED,RED,ORANGE,YELLOW)
MAP_CLOUDS  = (DARK_GREY,LIGHT_YELLOW,LIGHT_GREY,WHITE)

### set up
display_surf = pygame.display.set_mode((window_width, window_height))
display_surf.fill(WHITE)
tile = pygame.draw.rect(display_surf, BLACK, (0,200,tile_width,tile_height))
pygame.display.set_caption('Tiles')


###gameloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    #display_surf.fill(WHITE)
    # tile.blit(display_surf(100, 100))



    pygame.display.update()
