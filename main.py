import pygame

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("My First Pygame Window")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit loop if window is closed
    screen.fill((0, 128, 255))  # Fill screen with a color (RGB)
    pygame.display.flip()        # Update the display

pygame.quit()
