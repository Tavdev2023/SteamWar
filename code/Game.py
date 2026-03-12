import pygame
import self

from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        print("Setup Start") #Delete for Launch

        pygame.mixer_music.load('./assets/audio/MenuST.mp3')
        pygame.mixer_music.play(-1)

        while True: # Events Check
            menu = Menu(self.window)
            menu.run()
            pass




