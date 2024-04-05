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
pygame.display.set_caption("Key Press Events")

# Set the font for displaying text
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Print the event key when a key is pressed
            print("Key pressed:", event.key)
    
    # Fill the screen with white color
    screen.fill((255, 255, 255))
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# Quit Python
sys.exit()
