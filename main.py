from pygame.locals import *
from LabelModule import Label
from DashBoardModule import DashBoard
from GameModule import Game
from StartMenuModule import StartMenu
import pygame


def main():

    print("PROGRAM STARTED")
    programRunning = True

    while programRunning:
        screen = pygame.display.set_mode((1440, 810))

        # run start menu loop, waiting for user choose how many player is it.
        startMenu = StartMenu(screen)
        # return the number of players that user chosed2
        countAI = startMenu.run()

        print("number of AI:", countAI)
        newGame = Game(screen, countAI)  # create game object
        # Run the game loop, when gameover, return scores.
        newGame.initialize()
        scores = newGame.run()

        dashBoard = DashBoard(screen, scores)  # create dashBoard
        programRunning = dashBoard.run()  # run the dashBoard
    print("PROGRAM ENDED")


main()
