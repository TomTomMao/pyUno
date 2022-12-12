from pygame.locals import *
import pygame
from LabelModule import Label


class StartMenu:
    def __init__(self, screen):
        self.screen = screen

        self.hintLabel = Label(
            'Choose the number of AI players', (250, 50), 70, 'white')
        print("label setted up")

    def run(self):
        numberOfPlayer = None
        while numberOfPlayer == None:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 135 < x < 202 and 508 < y < 630:
                        numberOfPlayer = 2
                        return numberOfPlayer
                    elif 518 < x < 645 and 382 < y < 505:
                        numberOfPlayer = 3
                        return numberOfPlayer
                    elif 240 < x < 350 and 405 < y < 487:
                        numberOfPlayer = 4
                        return numberOfPlayer
                    elif 365 < x < 593 and 600 < y < 723:
                        numberOfPlayer = 5
                        return numberOfPlayer
                    elif 900 < x < 1140 and 600 < y < 720:
                        numberOfPlayer = 6
                        return numberOfPlayer
                    elif 755 < x < 1110 and 400 < y < 525:
                        numberOfPlayer = 7
                        return numberOfPlayer

                if event.type == QUIT:
                    quit()

            self.screen.blit(pygame.image.load('./Images/HomePage.jpg'), (0, 0))

            # These pictures are downloaded from the website: www.flaticon.com
            # 2 ducks
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (130, 510))
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (150, 510))

            # 3 ducks
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (510, 380))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (580, 415))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (580, 430))

            # 4 ducks
            self.screen.blit(pygame.image.load('./Images/duck.png'), (240, 405))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (250, 420))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (270, 405))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (290, 420))

            # 5 ducks
            self.screen.blit(pygame.image.load('./Images/duck.png'), (360, 640))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (380, 650))
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (410, 600))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (480, 600))
            self.screen.blit(pygame.image.load('./Images/duck4.png'), (480, 600))

            # 6 ducks
            self.screen.blit(pygame.image.load('./Images/duck.png'), (1000, 640))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (950, 600))
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (900, 600))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (1040, 610))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (1020, 600))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (1080, 650))

            # 7 ducks
            self.screen.blit(pygame.image.load('./Images/duck4.png'), (850, 380))
            self.screen.blit(pygame.image.load('./Images/duck4.png'), (880, 400))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (980, 480))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (1000, 430))
            self.screen.blit(pygame.image.load('./Images/duck3.png'), (1040, 450))
            self.screen.blit(pygame.image.load('./Images/duck.png'), (750, 450))
            self.screen.blit(pygame.image.load('./Images/duck2.png'), (780, 400))

            self.hintLabel.draw(self.screen)  # draw label
            pygame.display.flip()
