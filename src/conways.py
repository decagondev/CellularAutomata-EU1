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
    # pygame.draw.rect(screen, WHITE, pygame.Rect(20, 20, 20, 20))
    y = MARGIN
    i = 0  # counter variable
    while y < WIN_SIZE:
        x = MARGIN
        while x < WIN_SIZE:
            pygame.draw.rect(screen, BLACK, pygame.Rect(
                x, y, SQUARE_SIZE, SQUARE_SIZE))
            x += MARGIN + SQUARE_SIZE
        y += MARGIN + SQUARE_SIZE

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(5)

# Close the window and quit.
pygame.quit()
