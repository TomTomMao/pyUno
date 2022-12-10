import pygame
from StartMenuModule import StartMenu
from GameModule import Game
from LabelModule import Label
from pygame.locals import *


class DashBoard:
    def __init__(self, screen, returnValue):

        #                  returnValue={"winner":[{"ID":"player1"}],
        #                              "losers":[
        #                                        {"ID":"player0", "score":5, "cards":[CardBaseObject1, CardBaseObject2]},
        #                                        {"ID":"player1", "score":15, "cards":[CardBaseObject5, CardBaseObject25]}......
        #                                       ]
        #                              }
        self.screen = screen  # size: 1500*750
        self.winner = returnValue["winner"]  # length = 1
        self.losers = returnValue["losers"]  # length from 1 to 7

    def run(self):
        '''
            Render a gameover screen which displays players' information, use the information from self.winner and self.losers
            The screen would listen to user input and keep refreshing the page.
            Return: False if the user decides to quit the game.
            Return: True if the user decides to play a new turn.
            Note: player0 is the User, the rest players are the player
        '''
        print(self.winner)  # debug
        print(self.losers)  # debug


screen = pygame.display.set_mode((1500, 750))

gameResult = {"winner": [{"ID": "player1"}],
              "losers": [{"ID": "player0", "score": 5, "cards": ["red-1", "blue-2"]},
                         {"ID": "player1", "score": 15, "cards": ["green-5", "change-colour"]}]}
dashboard = DashBoard(screen, gameResult)
dashboard.run()

