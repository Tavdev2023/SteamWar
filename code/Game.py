import pygame
import self

from code.Menu import Menu


class Game():
    def __init__(self):
        pygame.init()
        window = pygame.display.set_mode(size=(800, 600))

    def run(self):

        print("Setup Start") #Delete for Launch

    while True:
        # Events check
        menu = Menu(self.window)
        menu.run()
        pass



