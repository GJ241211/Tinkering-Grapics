import pygame

pygame.init()

rect_side = 20

BLACK       = (  0,  0,  0)
DARK_ORANGE = (160, 75,  0)
DARK_YELLOW = (180,140,  0)
ORANGE      = (225,110,  0)
YELLOW      = (240,240, 50)

display_surf = pygame.display.set_mode((600, 600))

grid = []
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell

grid[5][5] = 20

for n in range(0, 10):
    grid[1][n] = 10
    grid[3][n] = 20
    grid[5][n] = 30
    grid[7][n] = 40

grid[8][5] = 10

def basic_tile(tile):
    pixel_array = pygame.PixelArray(tile)

    for x in range(rect_side):
        # Add an empty array that will hold each cell
        # in this row
        pixel_array.append([])
        for y in range(rect_side):
            pixel_array[x].append(0)

    for x in range (0, rect_side):
        for y in range (0, int(rect_side/2)):
            pixel_array[x][y] = 1
        for y in range(int(rect_side / 2), rect_side):
            pixel_array[x][y] = 2

    for x in range(0, rect_side):
        for y in range(0, rect_side):
            if pixel_array[x][y] == 1:
                color = YELLOW
                pixel_array[x][y] = color
            elif pixel_array[x][y] == 2:
                pixel_array[x][y] = color
                print (pixel_array[x][y])


    # pygame.draw.rect(display_surf, DARK_ORANGE, (0, 200, rect_side, rect_side))



while True:
    display_surf.fill(ORANGE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    for row in range(10):
        for column in range(10):
            color = BLACK
            tile = pygame.draw.rect(display_surf, color, [rect_side * column, rect_side * row, rect_side, rect_side])

            if grid[row][column] == 10:
                color = YELLOW
            elif grid[row][column] == 20:
                color = DARK_YELLOW
            elif grid[row][column] == 30:
                basic_tile(tile)



            #pygame.draw.rect(display_surf, color, [rect_side * column, rect_side * row, rect_side, rect_side])

    pygame.display.flip()
