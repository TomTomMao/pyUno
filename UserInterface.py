import random
import pygame
from LabelModule import Label
from pygame.locals import *
import time


class UserInterface:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

    def waitUserInput(self, candidateInput: list, hint):
        '''
            re
        '''
        print("it is your turn to:"+hint)
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.unicode in candidateInput:
                        return event.unicode

            self.renderOutput("it is your turn to:"+hint)

    def waitUserChooseColour(self):
        '''
            return : a string in ['blue','green','red','yellow']
        '''
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type ==KEYDOWN:
                    if event.unicode == 'b':
                        return 'blue'
                    if event.unicode == 'g':
                        return 'green'
                    if event.unicode == 'y':
                        return 'yellow'
                    if event.unicode == 'r':
                        return 'red'
            
            self.renderOutput("it is your turn to: choose the colour of the black card")
    
    def renderHint(self, hint):
        hintLabel = Label(hint, (100, 50), 50, "black")
        hintLabel.draw(self.screen)

    def renderKeyInfo(self):
        hintLabel = Label("press 1 to 9 choose chard", (600, 150), 50, "black")
        hintLabel.draw(self.screen)
        hintLabel2 = Label(
            "press 0 draw a card or skip the turn", (600, 200), 50, "black")
        hintLabel2.draw(self.screen)
        hintLabel2 = Label(
            "press r chose red, b chose blue, g chose green, y chose yellow", (600, 250), 50, "black")
        hintLabel2.draw(self.screen)

    def renderPlayersCards(self):
        y = 200
        for player in self.game.players:
            if player.isHuman:
                colour = "Black"
                humanPlayerLable = Label(
                    "You" + ": " + str(player.cards), (700, 700), 25, colour
                )
                humanPlayerLable.draw(self.screen)
                if player is self.game.currentPlayer:
                    playerLable = Label(
                        ">" + player.getID() + ": " +
                        f"has {str(len(player.cards))} cards", (50,
                                                                y), 25, colour
                    )
                else:
                    playerLable = Label(
                        player.getID() + ": " +
                        f"has {str(len(player.cards))} cards", (50,
                                                                y), 25, colour
                    )
            else:
                colour = "Red"
                if player is self.game.currentPlayer:
                    playerLable = Label(
                        ">" + player.getID() + ": " +
                        f"has {str(len(player.cards))} cards", (50,
                                                                y), 25, colour
                    )
                else:
                    playerLable = Label(
                        player.getID() + ": " +
                        f"has {str(len(player.cards))} cards", (50,
                                                                y), 25, colour
                    )
            y += 20
            playerLable.draw(self.screen)

    def renderDrawPile(self):
        drawPileLable = Label("drawPile: TOPCARD IS ??", (50, 500), 30, "blue")
        drawPileCountLable = Label(
            f"Number of Cards in DrawPile: {self.game.drawPile.count()}", (50, 550), 30, "blue")
        drawPileLable.draw(self.screen)
        drawPileCountLable.draw(self.screen)

    def renderDiscardPile(self):
        discardPileLabel = Label(
            f"Top Card of Discard Pile: {self.game.discardPile.showTopCard()}", (400, 500), 30, "blue")
        discardPileLabel.draw(self.screen)

    def renderOutput(self, hint):
        screen = self.game.screen

        screen.fill(pygame.Color("gray"))  # draw background
        self.renderKeyInfo()
        self.renderPlayersCards()
        self.renderDrawPile()
        self.renderDiscardPile()
        self.renderHint(hint)

        pygame.display.flip()
