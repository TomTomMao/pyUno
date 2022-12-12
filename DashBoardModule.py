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
        winner_dict = returnValue["winner"][0]
        winner_info = winner_dict["ID"]
        self.winner = winner_info  # length = 1

        # Take out the players and scores stored in the list dictionary
        losers_dict = returnValue["losers"]
        losers_dict.sort(key=lambda key: key['score'], reverse=True)
        losers_list = []
        for i in range(len(losers_dict)):
            info = losers_dict[i]["ID"] + "   " + "score: " + str(losers_dict[i]["score"])
            losers_list.append(info)
        # Store the retrieved information to the loser
        self.losers = losers_list  # length from 1 to 7
        pygame.font.init()


        imagePath = './Images/GameOver.jpg'
        self.screen.blit(pygame.image.load(imagePath), (0, 0))

    def run(self):
        '''
            Render a gameover screen which displays players' information, use the information from self.winner and self.losers
            The screen would listen to user input and keep refreshing the page.
            Return: False if the user decides to quit the game.
            Return: True if the user decides to play a new turn.
            Note: player0 is the User, the rest players are the player
        '''
        # This font is downloaded from the website: https://freefontsfamily.com
        font = pygame.font.Font('./fonts/times new roman bold italic.ttf', 40)
        # This font is downloaded from the website: https://font.chinaz.com
        font2 = pygame.font.Font('./fonts/farmbright.ttf', 150)
        #
        text1 = font.render("Winner " + str(self.winner), True, (65, 105, 225))
        text2 = font2.render("Game  over", True, (220, 226, 241))
        text3 = font.render('A New Round ', False, (255, 255, 255))
        text4 = font.render('Quit', True, (255, 255, 255))



        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 300 < x < 300 + 100 and 600 < y < 600 + 100:
                        return True
                    elif 900 < x < 900 + 100 and 600 < y < 600 + 100:
                        return False

            self.screen.blit(text1, (100, 100))
            self.screen.blit(text2, (800, 150))
            self.screen.blit(text3, (300, 600))
            self.screen.blit(text4, (900, 600))

            x, y = 100, 180
            for i in range(len(self.losers)):
                text = font.render("Loser  " + self.losers[i], True, (65, 105, 225))
                self.screen.blit(text, (x, y))
                y += 50

            pygame.display.flip()

# screen = pygame.display.set_mode((1500, 750))

# gameResult = {"winner": [{"ID": "player1"}],"losers": [{"ID": "player0", "score": 5, "cards": ["red-1", "blue-2"]},{"ID": "player1", "score": 15, "cards": ["green-5", "change-colour"]}]}
# dashboard = DashBoard(screen, gameResult)
# dashboard.run()
