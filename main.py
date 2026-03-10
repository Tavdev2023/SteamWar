import pygame

pygame.init()
window = pygame.display.set_mode(size = (800, 600))

while True:
    # Events check
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close window
            quit() # End Pygame