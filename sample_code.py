# imports

import pygame
import enum
import random

# variables

TILE_WIDTH = 32
TILE_HEIGHT = 32

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

MAP_WIDTH = 640
MAP_HEIGHT = 440
MAP_GAP = int(1 / 4 * MAP_WIDTH)

MAX_NUMBER_OF_TILES = [int(MAP_WIDTH / TILE_WIDTH), int(MAP_HEIGHT / TILE_HEIGHT / 3 * 4)]

# DRAWING_VARIABLES
ONE_THIRD_UP = int(1/3 * TILE_HEIGHT)
ONE_THIRD_ACROSS = int(1/3 * TILE_WIDTH)
HALF_ACROSS = int(1/2 * TILE_WIDTH)

MULTIPLIER = 1.4   # Determines how drastic the effects are on tiles

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (150, 40, 0)
DARK_ORANGE = (160, 75, 0)
DARK_YELLOW = (180, 140, 0)
ORANGE = (225, 110, 0)
YELLOW = (240, 240, 50)
TREE_GREEN = (90, 160, 40)
GRASS_GREEN = (90, 225, 40)
TREE_BROWN = (90, 60, 0)
DARK_GREY = (100, 100, 100)
DARK_BLUE = (0, 0, 140)
LIGHT_BLUE = (75, 240, 255)
LIGHT_GREY = (205, 205, 205)


class TileVariation(enum.Enum):
    NONE = 0
    DESERT = 1
    SNOWFIELD = 2
    FOREST = 3


class TileType(enum.Enum):
    BUILDING = 1
    TERRAIN = 2


class Tile:
    """Doc String"""

    def __init__(self, tile_type, tile_variant, x_position, y_position):
        self.tile_type = tile_type                                       # building or terrain
        self.tile_variant = tile_variant                                 # desert, forest, or snowfield
        self.x_position = x_position
        self.y_position = y_position

        self.surface = None
        if self.tile_type == TileType.BUILDING:
            self.surface = generate_building_tile()
        elif self.tile_type == TileType.TERRAIN:
            self.surface = generate_terrain_tile()

        if self.tile_variant == TileVariation.DESERT:
            self.surface = apply_desert_effect(self.surface)
        elif self.tile_variant == TileVariation.SNOWFIELD:
            self.surface = apply_snowfield_effect(self.surface)
        elif self.tile_variant == TileVariation.FOREST:
            self.surface = apply_forest_effect(self.surface)

    def print_properties(self):
        print(self.type + self.tile_variant +
              " @ (" + self.x_position + ", " +
              self.y_position + ")")


def generate_terrain_tile():
    # TODO: generate more interesting tiles
    tile_surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
    tile_surface.fill(TREE_BROWN)

    pygame.draw.rect(tile_surface, GRASS_GREEN, pygame.Rect(0, 0, TILE_WIDTH, ONE_THIRD_UP))
    pygame.draw.rect(tile_surface, DARK_GREY, pygame.Rect(0, TILE_HEIGHT-ONE_THIRD_UP, TILE_WIDTH, int(ONE_THIRD_UP * 2)))

    pygame.draw.line(tile_surface, GRASS_GREEN, (0, ONE_THIRD_UP+1), (ONE_THIRD_ACROSS, ONE_THIRD_UP+1), 3)
    pygame.draw.line(tile_surface, DARK_GREY, (HALF_ACROSS, int(ONE_THIRD_UP*2)), (TILE_WIDTH, int(ONE_THIRD_UP*2)), 3)

    return tile_surface


def generate_building_tile():
    # TODO:  RELATE TO TILE WIDTH AND HEIGHT
    tile_surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
    tile_surface.fill(BROWN)

    # TODO: experiment with pygame.draw to create more unique tiles //draws designs on tiles
    pygame.draw.rect(tile_surface, WHITE, pygame.Rect(0, 0, TILE_WIDTH - 1, TILE_HEIGHT - 1), 2)

    pygame.draw.line(tile_surface, WHITE, (0, ONE_THIRD_UP), (TILE_WIDTH, ONE_THIRD_UP), 2)
    pygame.draw.line(tile_surface, WHITE, (0, int(ONE_THIRD_UP*2)), (TILE_WIDTH, int(ONE_THIRD_UP*2)), 2)

    pygame.draw.line(tile_surface, WHITE, (HALF_ACROSS, 0), (HALF_ACROSS, ONE_THIRD_UP), 2)
    pygame.draw.line(tile_surface, WHITE, (HALF_ACROSS, int(ONE_THIRD_UP*2)), (HALF_ACROSS, TILE_HEIGHT), 2)

    pygame.draw.line(tile_surface, WHITE, (ONE_THIRD_ACROSS, ONE_THIRD_UP), (ONE_THIRD_ACROSS, int(ONE_THIRD_UP*2)), 2)
    pygame.draw.line(tile_surface, WHITE, (int(ONE_THIRD_ACROSS*2), ONE_THIRD_UP), (int(ONE_THIRD_ACROSS*2), int(ONE_THIRD_UP*2)), 2)



    return tile_surface


def apply_tile_effect(surface, tile_effect):
    if tile_effect == TileVariation.DESERT:
        return apply_desert_effect(surface)
    elif tile_effect == TileVariation.SNOWFIELD:
        return apply_snowfield_effect(surface)
    elif tile_effect == TileVariation.FOREST:
        return apply_forest_effect(surface)


def apply_desert_effect(surface):
    """Desert"""

    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):

            pixel = surface.get_at((x, y))
            new_red = int(pixel.r * MULTIPLIER)
            if new_red > 255:
                new_red = 255

            surface.set_at(
                (x, y),
                pygame.Color(new_red, pixel.g, pixel.b)
            )
    return surface


def apply_snowfield_effect(surface):
    """Snowfield"""

    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):

            pixel = surface.get_at((x, y))
            new_blue = int(pixel.b * MULTIPLIER)
            if new_blue > 255:
                new_blue = 255

            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, pixel.g, new_blue)
            )
    return surface


def apply_forest_effect(surface):
    """forest"""

    pixel = pygame.Color(0, 0, 0)
    for x in range(surface.get_width()):
        for y in range(surface.get_height()):

            pixel = surface.get_at((x, y))
            new_green = int(pixel.g / MULTIPLIER)
            if new_green > 255:
                new_green = 255

            surface.set_at(
                (x, y),
                pygame.Color(pixel.r, new_green, pixel.b)
            )
    return surface


def draw_tile(tile, canvas=pygame.Surface((1,1))):
    canvas.blit(tile.surface, (tile.x_position, tile.y_position))

######################################################## Unused code

def get_randomized_board():

    grid = []
    random.shuffle(My_tiles)

    my_tiles = []
    for x in range(MAX_NUMBER_OF_TILES[x, y]):
        MAX_NUMBER_OF_TILES = [x,y]
        for y in range(MAX_NUMBER_OF_TILES[x, y]):
            my_tiles.append(Tile(TileType.BUILDING,
                                 TileVariation.FOREST, 150, 100))
    return grid

########################################################### Unused code

def main():
    pygame.init()

    # TODO: randomly generate a set of tiles

    my_tile = Tile(TileType.BUILDING,
                   TileVariation.NONE,
                   100,
                   100)

    my_tiles = [my_tile]

    my_tiles.append(Tile(TileType.BUILDING,
                         TileVariation.FOREST, 150, 100))

    my_tiles.append(Tile(TileType.BUILDING,
                         TileVariation.DESERT, 200, 100))

    my_tiles.append(Tile(TileType.BUILDING,
                         TileVariation.SNOWFIELD, 250, 100))

    my_tiles.append(Tile(TileType.TERRAIN,
                         TileVariation.NONE, 100, 150))

    my_tiles.append(Tile(TileType.TERRAIN,
                         TileVariation.FOREST, 150, 150))

    my_tiles.append(Tile(TileType.TERRAIN,
                         TileVariation.DESERT, 200, 150))

    my_tiles.append(Tile(TileType.TERRAIN,
                         TileVariation.SNOWFIELD, 250, 150))

    display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surf.fill(BLACK)

        for tile in my_tiles:
            draw_tile(tile, display_surf)

        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
