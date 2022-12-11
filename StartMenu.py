# -*- coding: utf-8 -*-

import math
import sys
import pygame
from pygame.locals import *


if __name__=="__main__":

    pygame.init()
    screen = pygame.display.set_mode((1500, 750))
    pygame.display.set_caption("Choose the number of battle robots - Press")
    font = pygame.font.Font(None, 60)

    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)

class StartMenuZZ():
    def __init__(self,screen,font):
        self.screen=screen
        self.font=font
    def starmenurender():
        num_player=0
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, [450, 200, 100, 100])
        pygame.draw.rect(screen, GREEN, [850, 200, 100, 100])
        pygame.draw.rect(screen, GREEN, [450, 400, 100, 100])
        pygame.draw.rect(screen, GREEN, [850, 400, 100, 100])
        pygame.draw.rect(screen, GREEN, [450, 600, 100, 100])
        pygame.draw.rect(screen, GREEN, [850, 600, 100, 100])

        text = font.render('Choose the number of battle robots', True, (0, 0, 255), (0, 255, 0))
        text1 = font.render('2', True, (0, 0, 255), (0, 255, 0))
        text2 = font.render('3', True, (0, 0, 255), (0, 255, 0))
        text3 = font.render('4', True, (0, 0, 255), (0, 255, 0))
        text4 = font.render('5', True, (0, 0, 255), (0, 255, 0))
        text5 = font.render('6', True, (0, 0, 255), (0, 255, 0))
        text6 = font.render('7', True, (0, 0, 255), (0, 255, 0))

        screen.blit(text, (200, 100))
        screen.blit(text1, (480, 200))
        screen.blit(text2, (880, 200))
        screen.blit(text3, (480, 400))
        screen.blit(text4, (880, 400))
        screen.blit(text5, (480, 600))
        screen.blit(text6, (880, 600))


        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=event.pos
                    if 450 <x< 450+100 and 200<y<200+100:
                        num_player=2
                        return num_player
                    elif 850 <x< 850+100 and 200<y<200+100:
                        num_player=3
                        return num_player
                    elif 450 <x< 450+100 and 400<y<400+100:
                        num_player=4
                        return num_player
                    elif 850 <x< 850+100 and 400<y<400+100:
                        num_player=5
                        return num_player
                    elif 450 <x< 450+100 and 600<y<600+100:
                        num_player=6
                        return num_player
                    elif 850 <x< 850+100 and 600<y<600+100:
                        num_player=7
                        return num_player

            pygame.display.update()