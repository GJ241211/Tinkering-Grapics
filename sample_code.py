### imports

import pygame
import enum

### variables

TILE_WIDTH = 32
TILE_HEIGHT = 32

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

MAP_WIDTH  = 640
MAP_HEIGHT = 440
MAP_GAP    = int(1 / 4 * MAP_WIDTH)

MAX_NUMBER_OF_TILES = [int(MAP_WIDTH / TILE_WIDTH), int(MAP_HEIGHT / TILE_HEIGHT / 3 * 4)]

### Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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
    FOREST = 2
    SNOWFIELD = 3


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
        else:
            self.surface = generate_terrain_tile()

        if self.tile_variant == TileVariation.DESERT:
            self.surface = apply_desert_effect(self.surface)

    def print_properties(self):
        print(self.type + self.tile_variant +
              " @ (" + self.x_position + ", " +
              self.y_position + ")")


def generate_terrain_tile():
    # TODO: generate more interesting tiles
    tile_surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
    tile_surface.fill(GRASS_GREEN)
    return tile_surface


def generate_building_tile():
    # TODO: generate more interesting tiles
    tile_surface = pygame.Surface((TILE_WIDTH, TILE_HEIGHT))
    tile_surface.fill(LIGHT_GREY)

    # TODO: experiment with pygame.draw to create more unique tiles
    pygame.draw.rect(tile_surface, BLACK, pygame.Rect(0, 0, TILE_WIDTH - 1, TILE_HEIGHT - 1), 2)

    pygame.draw.rect(tile_surface, BLACK, pygame.Rect(int(TILE_WIDTH / 2),
                                                      int(TILE_WIDTH / 2),
                                                      1,
                                                      1), 2)

    return tile_surface


def apply_tile_effect(surface, tile_effect):
    if tile_effect == TileVariation.DESERT:
        return apply_desert_effect(surface)
    elif tile_effect == TileVariation.FOREST:
        pass
        #TODO
    else:
        pass
        #TODO

MULTIPLIER = 1.25
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

# TODO: add the other effects


def draw_tile(tile, canvas=pygame.Surface((1,1))):
    canvas.blit(tile.surface, (tile.x_position, tile.y_position))


def main():
    pygame.init()

    # TODO: randomly generate a set of tiles

    my_tile = Tile(TileType.BUILDING,
                   TileVariation.NONE,
                   100,
                   100)

    my_tiles = [my_tile]

    my_tiles.append(Tile(TileType.TERRAIN,
                         TileVariation.NONE, 200, 200))

    display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surf.fill(WHITE)

        for tile in my_tiles:
            draw_tile(tile, display_surf)

        pygame.display.update()

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
