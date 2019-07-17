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
initial_state = [0] * (SQUARES_PER_LINE * SQUARES_PER_LINE)

# randomize it
for x in range(SQUARES_PER_LINE):
    for y in range(SQUARES_PER_LINE):
        initial_state[x * SQUARES_PER_LINE + y] = random.randint(0, 1)
# TARGET ANY COORDINATES=> arr[x] = y * SQUARES_PER_LINE + x
# for i in range(len(initial_state)):
#     initial_state[i] = random.randint(0, 1)


# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    y = MARGIN
    i = 0  # counter variable
    while y < WIN_SIZE:
        x = MARGIN
        while x < WIN_SIZE:
            if initial_state[i] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            x += MARGIN + SQUARE_SIZE
            i += 1
        y += MARGIN + SQUARE_SIZE

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
