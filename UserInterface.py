import random
import pygame
from LabelModule import Label
from pygame.locals import *
import time


class UserInterface:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen

        # a list of user's hand

    def waitUserInput(self, candidateInput: list, hint):
        userHand = self.game.getPlayerByID("player0").cards
        '''
            candidateInput: a list of numbers that refer to the index of the legal cards in the userHand
                If there is no -1 in the list, it is waiting for the user choose the card to swap.
                The possible minimun number of candidateInput is -1 (which means not play a card)
                The possible maximun number of candidateInput is len(self.userHand) - 1 
            hint: hint text that would display on the screen
            According to the user's input(either mouse or keyboard) at pygame, 
                Return an int that is the index of the card in self.userHand that the user wish to choose if the int is in the candidateInput.
            Return -1 if user don't want play a card AND if -1 is in candidateInput.(Note: The user may or may not draw a new card.)
        '''
        print(hint)
        print(candidateInput)
        # ignore the event that was not raised here

        for event in pygame.event.get():
            pass
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    print(
                        f"--------------------user key:{event.unicode}-------------")
                    if event.unicode == "0" and -1 in candidateInput:
                        return -1
                    elif event.unicode in [str(i+1) for i in candidateInput]:
                        return int(event.unicode)-1
                    else:
                        print("Please make a valid decision")

            self.renderOutput(hint)

    def waitUserChooseColour(self):
        '''
            According to the user's input in pygame,
            return : a string in ['blue','green','red','yellow']
        '''

        # ignore the event that was not raised here
        for event in pygame.event.get():
            pass
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.unicode == 'b':
                        return 'blue'
                    if event.unicode == 'g':
                        return 'green'
                    if event.unicode == 'y':
                        return 'yellow'
                    if event.unicode == 'r':
                        return 'red'

            self.renderOutput(
                "it is your turn to: choose the colour of the black card")

    def renderHint(self, hint):
        hintLabel = Label(hint, (100, 50), 50, "black")
        hintLabel.draw(self.screen)

    def renderKeyInfo(self):
        hintLabel = Label("press 1 to 9 choose chard", (500, 150), 30, "black")
        hintLabel.draw(self.screen)
        hintLabel2 = Label(
            "press 0 draw a card or skip the turn", (500, 200), 30, "black")
        hintLabel2.draw(self.screen)
        hintLabel2 = Label(
            "press r chose red, b chose blue, g chose green, y chose yellow", (500, 250), 30, "black")
        hintLabel2.draw(self.screen)

    def renderPlayersCards(self):
        y = 200
        for player in self.game.players:
            if player.isHuman:
                colour = "Black"
                humanPlayerLable = Label(
                    "You" + ": " + str(player.cards), (300, 700), 25, colour
                )
                humanPlayerLable.draw(self.screen)

                # the left-up corner that display all the players ">"refer to the current player
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
        topCard = self.game.discardPile.showTopCard()  # the top card on the discard pile
        topCardColour, topCardType, topCardChosenColour = topCard.cardColour, topCard.type, topCard.chosenColour
        # print(topCardColour, topCardType, topCardChosenColour)
        discardPileLabel = Label(
            f"Top Card of Discard Pile: {topCard}", (400, 500), 30, "blue")
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
