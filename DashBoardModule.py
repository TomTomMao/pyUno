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
        pygame.font.init()

    def run(self):
        '''
            Render a gameover screen which displays players' information, use the information from self.winner and self.losers
            The screen would listen to user input and keep refreshing the page.
            Return: False if the user decides to quit the game.
            Return: True if the user decides to play a new turn.
            Note: player0 is the User, the rest players are the player
        '''

        font = pygame.font.Font('/HFPuff/HFPuff-2.ttf', 70)

        text1 = font.render('"Winner =" ,"self.winner"', True, (0, 0, 255), (0, 255, 0))
        text2 = font.render('"Loser=" ,"self.losers"', True, (0, 0, 255), (0, 255, 0))
        text3 = font.render('A New Round ', True, (0, 0, 255), (0, 255, 0))
        text4 = font.render('Quit', True, (0, 0, 255), (0, 255, 0))
        def get_score (element):
            return element['score']

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 300 < x < 300+ 100 and 600 < y < 600 + 100:
                        num_player = 2
                        return False
                    elif 900 < x < 900 + 100 and 600 < y < 600 + 100:
                        return True

            print(self.winner)  # debug


            self.losers.sort(key= get_score)
            print(self.losers)  # debug

            self.screen.blit(text1, (400, 100))
            self.screen.blit(text2, (400, 200))
            self.screen.blit(text3, (300, 600))
            self.screen.blit(text4, (900, 600))

            pygame.display.flip()


#screen = pygame.display.set_mode((1500, 750))

#gameResult = {"winner": [{"ID": "player1"}],"losers": [{"ID": "player0", "score": 5, "cards": ["red-1", "blue-2"]},{"ID": "player1", "score": 15, "cards": ["green-5", "change-colour"]}]}
#dashboard = DashBoard(screen, gameResult)
#dashboard.run()
