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

                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 450 <x< 450+100 and 200<y<200+100:
                        numberOfPlayer=2
                        return numberOfPlayer
                    elif 850 <x< 850+100 and 200<y<200+100:
                        numberOfPlayer = 3
                        return numberOfPlayer
                    elif 450 <x< 450+100 and 400<y<400+100:
                        numberOfPlayer = 4
                        return numberOfPlayer
                    elif 850 <x< 850+100 and 400<y<400+100:
                        numberOfPlayer = 5
                        return numberOfPlayer
                    elif 450 <x< 450+100 and 600<y<600+100:
                        numberOfPlayer = 6
                        return numberOfPlayer
                    elif 850 <x< 850+100 and 600<y<600+100:
                        numberOfPlayer = 7
                        return numberOfPlayer

                if event.type == QUIT:
                    quit()

           #This font comes from the font encyclopedia of the Internet,
            # this is the URL of the font source: "https: // www.fonts.net.cn / fonts - en / tag - katong - 1.html"
            font = pygame.font.Font('/Users/lizongzhe/Desktop/Nottingham/pythonProject/coursework/HFPuff/HFPuff-2.ttf',
                                    70)
            GREEN = (0, 255, 0)
            BLUE = (0, 0, 255)
            BLACK = (0, 0, 0)

            text = font.render('Choose the number of battle robots', True, (0, 0, 255), (0, 255, 0))
            text1 = font.render('2', True, (0, 0, 255), (0, 255, 0))
            text2 = font.render('3', True, (0, 0, 255), (0, 255, 0))
            text3 = font.render('4', True, (0, 0, 255), (0, 255, 0))
            text4 = font.render('5', True, (0, 0, 255), (0, 255, 0))
            text5 = font.render('6', True, (0, 0, 255), (0, 255, 0))
            text6 = font.render('7', True, (0, 0, 255), (0, 255, 0))



            self.screen.fill(pygame.Color("blue"))  # draw background

            self.screen.blit(text, (200, 100))
            self.screen.blit(text1, (480, 200))
            self.screen.blit(text2, (880, 200))
            self.screen.blit(text3, (480, 400))
            self.screen.blit(text4, (880, 400))
            self.screen.blit(text5, (480, 600))
            self.screen.blit(text6, (880, 600))

            self.hintLabel.draw(self.screen)  # draw label
            pygame.display.flip()


