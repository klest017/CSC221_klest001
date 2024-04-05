import pygame
import sys

class Rocket:
    def __init__(self, screen):
        # Load rocket image
        self.image = pygame.image.load("rocket.png")  
        self.rect = self.image.get_rect()
        
        # Set the initial position of the rocket at the center of the screen
        self.rect.center = screen.get_rect().center
        
    def update(self, keys):
        # Update rocket position based on key inputs
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        
        # Ensure rocket stays within screen boundaries
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, screen):
        # Draw rocket on the screen
        screen.blit(self.image, self.rect)

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
window_width = 800
window_height = 600
window_size = (window_width, window_height)

# Create the Pygame window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Rocket Game")

# Load rocket image and create rocket object
rocket = Rocket(screen)

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()

    # Update rocket position based on key inputs
    rocket.update(keys)

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Draw the rocket
    rocket.draw(screen)
    
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

# Quit Python
sys.exit()
