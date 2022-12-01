from pygame.locals import *
import pygame
from LabelModule import Label


class DashBoard:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def run(self):
        numberOfPlayer = None
        while numberOfPlayer == None:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.unicode == "q":
                        return False
                    else:
                        return True
                if event.type == QUIT:
                    return False

            y = 100

            self.screen.fill(pygame.Color("blue"))  # draw background
            for player in self.game.players:

                playerLabel = Label(player.getID(
                ) + ", Score: " + str(player.getScore()) + ", cards lefted: " + str(len(player.cards)), (50, y), 30, "white")
                playerLabel.draw(self.screen)
                y += 35

            hintLabel = Label(
                "GameOver Press any key for keep playing, press Q quit the game", (50, 50), 30, 'white')
            hintLabel.draw(self.screen)  # draw label
            pygame.display.flip()
