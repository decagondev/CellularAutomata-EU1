import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
MARGIN = 3
SQUARE_SIZE = 20
SQUARES_PER_LINE = 25

#  calculate the windowns size dynamically
WIN_SIZE = (SQUARES_PER_LINE + 1) * MARGIN + SQUARES_PER_LINE * SQUARE_SIZE


pygame.init()

# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Set up initial state
row = [0] * SQUARES_PER_LINE
initial_state = []
for i in range(SQUARES_PER_LINE):
    initial_state.append(row.copy())

# randomize it
for r in range(SQUARES_PER_LINE):
    for col in range(SQUARES_PER_LINE):
        initial_state[r][col] = random.randint(0, 1)


# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Get alive neighbours:
def get_alive_neighbours(row, col, arr, row_len):
    alive_neighbours = 0

    left = col - 1 >= 0
    right = col + 1 < row_len
    top = row - 1 >= 0
    bot = row + 1 < row_len

    # left
    if left and arr[row][col - 1]:
        alive_neighbours += 1

    # right
    if right and arr[row][col + 1]:
        alive_neighbours += 1

    # top
    if top and arr[row - 1][col]:
        alive_neighbours += 1

    # top left
    if top and left and arr[row - 1][col - 1]:
        alive_neighbours += 1

    # top right
    if top and right and arr[row - 1][col + 1]:
        alive_neighbours += 1

    # bot
    if bot and arr[row + 1][col]:
        alive_neighbours += 1

    # bot left
    if bot and left and arr[row + 1][col - 1]:
        alive_neighbours += 1

    # bot right
    if bot and right and arr[row + 1][col + 1]:
        alive_neighbours += 1

    return alive_neighbours


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    for r in range(len(initial_state)):
        for c in range(len(initial_state[0])):
            # check state of neigbours here
            alive_neighbours = get_alive_neighbours(
                r, c, initial_state, SQUARES_PER_LINE)

        # based on number of dead or alive neighbours update new state

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    y = MARGIN
    r = 0
    while y < WIN_SIZE:
        c = 0
        x = MARGIN
        while x < WIN_SIZE:
            if initial_state[r][c] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            x += MARGIN + SQUARE_SIZE
            c += 1
        r += 1
        y += MARGIN + SQUARE_SIZE

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
