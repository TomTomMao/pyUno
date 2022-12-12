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
        screen = pygame.display.set_mode((1500, 750))

        # run start menu loop, waiting for user choose how many player is it.
        startMenu = StartMenu(screen)
        # return the number of players that user chosed2
        countAI = startMenu.run()

        print("number of AI:", countAI)

        # This music is downloaded from the website: https://audionautix.com/
        # Initialize the bgm
        pygame.mixer.init()
        pygame.mixer.music.load("./Audio/90SecondsOfFunk.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.2)

        newGame = Game(screen, countAI)  # create game object
        # Run the game loop, when gameover, return scores.
        newGame.initialize()
        scores = newGame.run()


        dashBoard = DashBoard(screen, scores)  # create dashBoard
        pygame.mixer.music.stop()
        programRunning = dashBoard.run()  # run the dashBoard
    print("PROGRAM ENDED")


if __name__ == '__main__':
    main()
