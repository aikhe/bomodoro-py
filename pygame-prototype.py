import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set window dimensions
width, height = 400, 300

# Set transparency color
transparent_color = (0, 0, 0, 0)  # Fully transparent

# Create the window
screen = pygame.display.set_mode((width, height), pygame.SRCALPHA)

# Set the window title
pygame.display.set_caption("Transparent Window Example")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    # Fill the window with transparent color
    screen.fill(transparent_color)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

