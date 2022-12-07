import random
import pygame
from LabelModule import Label
from pygame.locals import *
import time
from UserInterface import UserInterface


class CardBase:
    def __init__(self) -> None:
        pass

    def checkCard(topDiscardCard, cardToPlay):
        '''
            given topDiscardCard, check if cardToPlay is legal
            Return True if it is legal
            Return False otherwise
        '''
        return topDiscardCard.type == cardToPlay.type or topDiscardCard.cardColour == cardToPlay.cardColour

    def getImage(self):
        '''
            return an image object
        '''


class NumberCard(CardBase):
    def __init__(self, cardColour: str, cardType: str, cardID: int = -1):
        # cardColour: a string
        # cardType: a string
        # cardID: a number

        self.cardColour = cardColour  # a string
        self.type = cardType  # a string
        self.cardID = "card" + str(cardID)  # a string
        self.value = {'green': 1, 'red': 2, 'yellow': 3,
                      'blue': 4}[cardColour]*int(self.type)

    def __repr__(self):
        return self.cardColour + "-" + self.type


class Owner:
    '''
    A class that would be input into a CardManager Object
    '''

    def __init__(self) -> None:
        pass


class Player(Owner):
    def __init__(self, playerID: int, isHuman: bool = False):
        # playerID is an int
        # all player should share different id
        self.playerID = 'player' + str(playerID)
        self.isHuman = isHuman
        self.cards = []

    def getScore(self):
        cardScores = [int(card.value) for card in self.cards]
        return sum(cardScores)

    def getID(self):
        return self.playerID

    def __repr__(self):
        if self.isHuman:
            return "type: Human" + ", playerID: " + self.getID() + "cards:" + self.cards.__repr__()
        else:
            return "type: AI" + ", playerID: " + self.getID() + "cards:" + self.cards.__repr__()

    def addCard(self, card):
        self.cards.append(card)

    def removeCard(self, cardToRemove):
        self.cards = [card for card in self.cards if card is not cardToRemove]

    def swapCard(self, game, topDiscardCard, userInterface):
        '''
            If the player is computer, return a random valid card
            Waiting for the player choosing a card to swap;
            Once the player choose a card, return the card;
        '''
        if self.isHuman == False:
            print(self.playerID + "is swapping card")
            return (self.cards[random.randint(0, len(self.cards)-1)])
        while True:
            userInput = userInterface.waitUserInput(
                [str(i) for i in range(1, 10)], "swap card.")
            indexOfCard = int(userInput)

            if indexOfCard < len(self.cards) + 1:
                return (self.cards[indexOfCard - 1])

            userInterface.renderOutput("Please choose a valid card")

    def playCard(self, game, topDiscardCard, userInterface):
        '''4
            If the player is computer, return a random valid card
            waiting for the player making a decision, either choose to play a valid card, or choose not to play a card.
            If play a card, return the valid card player choosed
            If choose not to play a card, return False
        '''
        if self.isHuman == False:
            print(self.playerID + "is playing card")
            validCards = [card for card in self.cards if CardBase.checkCard(
                topDiscardCard, card)]
            if len(validCards) > 0:
                cardToPlay = random.choice(validCards)
                print(self.playerID + f"decide to play {cardToPlay}")
                return cardToPlay
            else:
                print(self.playerID +
                      "decide not to play any card, and it would draw a card")
                return False
        while True:
            userInput = userInterface.waitUserInput(
                [str(i) for i in range(0, 10)], "play a card."
            )
            indexOfCard = int(userInput)
            if indexOfCard == 0:  # press 0 to not play a card
                return False
            elif indexOfCard < len(self.cards) + 1:
                cardToPlay = self.cards[indexOfCard - 1]
                print("cardToPlay:", cardToPlay)
                if CardBase.checkCard(topDiscardCard, cardToPlay):
                    return cardToPlay


class DrawPile(Owner):
    '''
        An object that maintain an order of a list of cards, and the card count information
        Support push a card on the top,
        Support pop the a card on the top
        Support reveal the card count information
    '''

    def __init__(self, cards):
        # put cards into drawpile
        self.cards = cards  # a list of cards, the first element in the list is the buttom of the drawPile, last element in the list is the top of the drawPile

        random.shuffle(self.cards)
        self.drawPileID = "drawPile"

    def count(self):
        '''
            return the number of cards in the draw pile
        '''
        return len(self.cards)

    def getID(self):
        return self.drawPileID

    def popTopCard(self):
        '''
            assume there is at least a card, assume all cards in self.cards belongs to the drawPile
            This function won't change the ownership information, so you need to manually change the ownership information
            This function will remove the top card of the drawPile
            return the Top card
        '''
        topCard = self.cards[-1]
        self.cards = self.cards[:-1]
        print("number of Card In draw pile:", len(self.cards))
        return topCard

    def __repr__(self):
        return reversed(self.cards).__repr__()


class DiscardPile(Owner):
    '''
        An object that maintain an order of a list of cards, and the card count information
        Support push a card on the top,
        Support get the information of a card on the top
        Support reveal the card count information
    '''

    def __init__(self):
        self.cards = []  # the first is buttom. the last is top.
        self.discardPileID = "discardPile"

    def getID(self):
        return self.discardPileID

    def pushCardOnTop(self, card: CardBase):
        self.cards.append(card)

    def pushCardToButtom(self, newCard: CardBase):
        tmpCards = [newCard]
        for card in self.cards:
            tmpCards.append(card)
        self.cards = tmpCards

    def showTopCard(self):
        '''
            assume there is at least one card in this object, return the information of the top card.
        '''
        return self.cards[-1]

    def __repr__(self):
        return reversed(self.cards).__repr__()


class CardManager:
    '''
        A Class maintain ownership information.
    '''

    def __init__(self, players: list, drawPile: DrawPile, discardPile: DiscardPile):

        self.players = players
        self.drawPile = drawPile
        self.discardPile = discardPile
        # store the ownership data, mapping ownerID to a list of cards belong to the owner
        self.ownership = {}

        for player in self.players:
            self.registerPlayer(player.getID())
        self.registerDrawPile(self.drawPile.getID())
        self.registerDiscardPile(self.discardPile.getID())

    def registerPlayer(self, playerID: str):
        self.ownership[playerID] = []

    def registerDrawPile(self, drawPileID: str):
        self.ownership[drawPileID] = []

    def registerDiscardPile(self, discardPileID: str):
        self.ownership[discardPileID] = []

    def getOwnerObject(self, card: CardBase):
        '''
            given a card object
            return the owner of the card (which is a player or a drawPile or a discardPile object)
            if the card does not have an owner, return None
            Can be used for check if a card belong to the user, and decide how to render them
        '''
        if card in self.ownership[self.drawPile.drawPileID]:
            return self.drawPile
        elif card in self.ownership[self.discardPile.discardPileID]:
            return self.discardPile
        else:
            for player in self.players:
                if card in self.ownership[player.playerID]:
                    return player
            return None

    def moveCard(self, cardToMove: CardBase, newOwner: Owner):
        '''
            if the card has an owner, delete the old ownership, assign the cardToMove to the newOwner
            if the card doesn't have any owner, assign the cardToMove to the newOwner
            Note: this function only change the ownership data in this.ownership, won't change the newOwner.cards
        '''
        oldOwner = self.getOwnerObject(cardToMove)
        if oldOwner != None:
            self.ownership[oldOwner.getID()] = [
                card for card in self.ownership[oldOwner.getID()] if card is not cardToMove]
        self.ownership[newOwner.getID()].append(cardToMove)

    def getCardsByOwner(self, owner: Owner):
        '''
            assume the owner is already registered
            owner: a player object or a drawpile object or a discard pile object
            Return: a list of cards belongs to the owner
        '''
        return self.ownership[owner.getID()]

    def __repr__(self) -> str:
        return str(self.ownership)


class Behaviour:
    '''
        behaviour that player or dealer can do, used for making sure that cards ownership is consistent in Owner's records and CardManager's record
        control the cards of players and piles, also update card owner information.
        always call the function in this class when human or computer want to play card, or when the game is initializing.
    '''


class Game:

    def __init__(self, screen: pygame.Surface, countAI) -> None:
        self.screen = screen
        self.countAI = countAI
        self.cardManager = None
        self.players = []
        self.direction = 1  # not reversed
        self.drawPile = None
        self.discardPile = None
        self.playerDictionary = {}
        self.userInterFace = UserInterface(self)

    def __checkCardConsistency__(self):
        '''
            Compare players' card and ownership Data
        '''
        for i in range(self.countAI + 1):
            checkingPlayer = self.getPlayerByID(f"player{i}")

            if (set(self.cardManager.getCardsByOwner(checkingPlayer)) != set(checkingPlayer.cards)):
                raise Exception(
                    "Cards are not consistent between owner and cardManager, player" +
                    f"{i}.cards = {checkingPlayer.cards}; but self.cardManager.getCardsByOwner(player{i})" +
                    f" = {self.cardManager.getCardsByOwner(checkingPlayer)}")
        if set(self.cardManager.getCardsByOwner(self.discardPile)) != set(self.discardPile.cards):
            manageCards = self.cardManager.getCardsByOwner(self.discardPile)
            raise Exception("Cards are not consistent between owner and cardManager, self.discardPile." +
                            f"cards = {self.discardPile.cards}; but self.cardManager.getCardsByOwner(self.discardPile)" +
                            f" = {manageCards}")
        return True

    def givePlayerCard(self, player: Player):
        '''
            player: a Player object.
            assume self.drawpile is not None
            assume there is at least a card in the self.drawPile
            assume self.discardPile is not None
            remove the first card from self.drawPile
            Delete the ownership between this card and the self.draWPile
            Assign the ownership of this card to the player
            Return the card given to the player
        '''
        print("giving ", player.playerID, "a card")
        topCard = self.drawPile.popTopCard()
        self.cardManager.moveCard(topCard, player)
        player.addCard(topCard)
        return topCard

    def getPlayerByID(self, playerID: str):
        '''
            playerID: player's ID
            return player Object
        '''
        return self.playerDictionary[playerID]

    def playerPlayCard(self, player: Player, cardToPlay):
        '''
            Assume the cardToPlay is legal to play
            remove the card from the player.cards
            change the ownership of the card from player to self.discardPile
            put the card to the top of the self.discardPile
        '''
        player.removeCard(cardToPlay)
        self.cardManager.moveCard(cardToPlay, self.discardPile)
        self.discardPile.pushCardOnTop(cardToPlay)

    def checkWinner(self):
        '''
            return True if anyone has no card
            otherwise return False
        '''
        for player in self.players:
            if len(self.cardManager.getCardsByOwner(player)) == 0:
                return True
        return False

    def initialize(self):
        self.currentPlayerIndex = -1
        self.playDirection = 1
        self.countPlayer = self.countAI + 1

        # create players
        # choose the first one as human
        self.players.append(Player(0, True))
        for i in range(1, self.countAI + 1):
            self.players.append(Player(i))
        print("players created")

        # shuffle the players
        random.shuffle(self.players)

        for player in self.players:  # for faster look up by id
            self.playerDictionary[player.getID()] = player

        # generate a deck of cards
        cardColours = ["red", "green", "blue", "yellow"]
        cardTypes = ["0", "1", "2", "3", "4", "5", "6", "7", "8",
                     "9", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        cards = [NumberCard(cardColour, cardType, -1)
                 for cardColour in cardColours for cardType in cardTypes]
        # set id for each card
        for i in range(len(cards)):
            cards[i].cardID = i

        # create draw pile and discard pile
        self.drawPile = DrawPile(cards)  # put all cards on the draw pile
        print("size of the deck: ", len(self.drawPile.cards))
        self.discardPile = DiscardPile()

        self.cardManager = CardManager(
            self.players, self.drawPile, self.discardPile)

        for card in self.drawPile.cards:  # create the ownership of cards in drawPile
            self.cardManager.moveCard(card, self.drawPile)

        # give each player 7 cards

        for player in self.players:  # for each player
            for _ in range(7):  # give the player 7 cards
                self.givePlayerCard(player)

        # choose the first card
        firstCard = self.drawPile.popTopCard()
        # update the ownership
        self.cardManager.moveCard(firstCard, self.discardPile)
        # and put the card on the discard pile
        self.discardPile.pushCardOnTop(firstCard)
        print(f"draw the first card: {firstCard}")

    def run(self):

        # play the game
        isGameOver = False
        while isGameOver == False:
            # Set the current player
            self.currentPlayerIndex = (
                self.currentPlayerIndex + 1) % self.countPlayer
            self.currentPlayer: Player = self.players[self.currentPlayerIndex]
            currentPlayer = self.currentPlayer
            # self.userInterFace.renderOutput("computer is playing")
            # time.sleep(1)
            print(f"\n\n\n\n\n{currentPlayer.getID()}'s turn start")
            #
            #
            #
            #
            #
            # check if the top card in discard Pile is forbid, if so, set currentPlayer tobe the next player
            # inplement in future
            #
            #
            #
            #
            #
            #
            if (self.drawPile.count() != 0):
                # 1**************************player swap card input start**************************
                # Wait for player input: chose the card (a infinite loop here), mean while render the screen
                cardToSwap: CardBase = currentPlayer.swapCard(  # player.swapCard hasn't been defined, it should be: A loop wait for user choose a card, return the card object user choosed
                    self, self.discardPile.showTopCard(),  self.userInterFace)  # the input of top card might not be necessary as user can see the screen and computer can access data
                # at this line, the player has already chosed the card
                # **************************player swap card input end**************************
                #
                # **************************data manipulating start**************************
                # Manipulating the data of the game:
                # move cardToSwap from the currentPlayer to the top of discardPile,
                if len(self.drawPile.cards) > 0:
                    currentPlayer.removeCard(cardToSwap)  # REFactor
                    self.cardManager.moveCard(
                        cardToSwap, self.discardPile)  # REFactor
                    self.discardPile.pushCardToButtom(cardToSwap)  # REFactor

                    # give currentPlayer a new card from the top of the drawPile

                    cardSwapped = self.givePlayerCard(currentPlayer)
                # **************************data manipulating end**************************
                #
                # ***************rendering animation start***************
                if currentPlayer.isHuman:
                    # this could be pygame animation
                    self.userInterFace.renderOutput(
                        f"you swapped a card, old card: {str(cardToSwap)}, new card: {str(cardSwapped)}")
                    time.sleep(3)

                # this could be pygame animation
                else:
                    self.userInterFace.renderOutput(
                        f"{currentPlayer.getID()} swapped a card")
                    time.sleep(3)

            # ***************rendering animation over***************
            #
            #
            #
            #
            #
            #
            #
            #
            #
            # in future: check if the top card is draw special card if so , manipulating data and render draw special cards
            #
            #
            #
            #
            #
            #
            #
            #
            # 2**************************player first play card input start**************************
            # wait for player Input: choose a valid card, or choose to play no card
            cardToPlay: CardBase = currentPlayer.playCard(self, self.discardPile.showTopCard(
            ),  self.userInterFace)  # return the valid card player choosed
            # 2**************************player first play card input end**************************
            if cardToPlay != False:  # if play a card (2.1)
                # 2.1**************************data manipulating start**************************
                # if so, manipulating the data of the game:
                self.playerPlayCard(currentPlayer, cardToPlay)
                # 2.1**************************data manipulating end**************************
                #
                # 2.1***************rendering animation start***************
                if currentPlayer.isHuman:
                    self.userInterFace.renderOutput(
                        f"Your played this card: {str(cardToPlay)}")
                    time.sleep(3)
                else:
                    self.userInterFace.renderOutput(
                        f"{currentPlayer.getID()} played this card: {str(cardToPlay)}")
                    time.sleep(3)

                # 2.1***************rendering animation end***************
                # if there is a winner, loop end; other wise keep looping
                # note isGameOver would become false if there is a winner, thus loop end and go back to main.py
                isGameOver = self.checkWinner()
                if isGameOver:
                    return self.getResult()
                else:
                    # go next player, but we don't need to increment data here.
                    pass
                #
                #
                #
                #
            elif cardToPlay == False:  # player choose not to play a card (2.2)
                # give player a new card
                # Manipulating data of the game:
                # 2.2**************************data manipulating start**************************
                if len(self.drawPile.cards) > 0:  # if there is a card in draw pile
                    cardToGive = self.givePlayerCard(currentPlayer)
                    print("---------------------flag1---------------------")
                # 2.2**************************data manipulating end**************************
                #
                #
                #
                #
                # 2.2***************rendering animation start***************
                    print(
                        f"you are drawing a card({cardToGive}) from the top of the draw pile... you hand and card are both moving...")  # this could be animiation
                # 2.2***************rendering animation end***************
                #
                #
                #
                #
                    # 2.2**************************player second play card input start**************************
                    # wait for player Input: choose a valid card, or choose to play no card
                    cardToPlay: CardBase = currentPlayer.playCard(self, self.discardPile.showTopCard(
                    ),  self.userInterFace)  # return the valid card player choosed
                    # 2.2**************************player secone play card input end**************************
                    if cardToPlay != False:  # if play a second card (2.2.1)
                        print("---------------------flag2---------------------")
                        # 2.2.1**************************data manipulating start**************************
                        # if so, manipulating the data of the game:
                        self.playerPlayCard(currentPlayer, cardToPlay)
                        # 2.2.1**************************data manipulating end**************************
                        #
                        # 2.2.1***************rendering animation start***************
                        print(
                            f"Your played this card: {str(cardToPlay)} card is moving from your hand to the discard pile...")  # this could be animiation
                        # 2.2.1***************rendering animation end***************
                        # if there is a winner, return back to main.py
                        isGameOver = self.checkWinner()
                        if isGameOver:
                            return self.getResult()
                        else:
                            # go next loop
                            pass
                    else:  # player don't play a second card
                        print("---------------------flag3---------------------")

                        pass  # go next loop

            print(f"{currentPlayer.getID()}'s turn end\n\n\n\n\n")
        print("gameOver")
        return self.getResult()
        # game over, return result

    def getResult(self):
        winner = [player for player in self.players if len(
            player.cards) == 0][0]
        losers = [player for player in self.players if len(player.cards) != 0]
        returnValue = {
            "winner": [{"ID": winner.getID()}],
            "losers": [{"ID": loser.getID(), "score": loser.getScore(), "cards": loser.cards} for loser in losers]
        }

        return returnValue
        # returnValue looks like this:{"winner":[{"ID":"player1"}],
        #                              "losers":[
        #                                        {"ID":"player0", "score":5, "cards":[CardBaseObject1, CardBaseObject2]},
        #                                        {"ID":"player1", "score":15, "cards":[CardBaseObject5, CardBaseObject25]}......
        #                                       ]
        #                             }

# screen = pygame.display.set_mode((1500, 900))
# game = Game(screen, 2)
# game.initialize()
# game.run()
