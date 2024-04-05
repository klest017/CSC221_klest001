#TIY 12-1

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600
window_size = (window_width, window_height)

# Create the Pygame window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Blue Window")

# Set the background color (RGB values)
background_color = (0, 0, 255)  # Blue color

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with the background color
    screen.fill(background_color)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# Quit Python
sys.exit()

