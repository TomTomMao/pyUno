from pygame.locals import *
import pygame
from LabelModule import Label


class StartMenu:
    def __init__(self, screen):
        self.screen = screen
        self.hintLabel = Label(
            'Press number of ai players(1 to 7)', (100, 100), 72, 'green')
        print("label setted up")

    def run(self):
        numberOfPlayer = None
        while numberOfPlayer == None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if (1 <= event.key - 48 <= 7):
                        return event.key - 48
                    else:
                        print("invalid key")
                if event.type == QUIT:
                    quit()

            self.screen.fill(pygame.Color("blue"))  # draw background
            self.hintLabel.draw(self.screen)  # draw label
            pygame.display.flip()
