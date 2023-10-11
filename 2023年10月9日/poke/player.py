import random

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def deal(self, card):
        self.cards.append(card)

    def play(self):
        randomIndex = random.randint(0, len(self.cards) - 1)
        playCard = self.cards.pop(randomIndex)
        print(self.name, "出牌:", [playCard.color, playCard.number])
        return playCard
    
    def checkIsNoCards(self):
        return len(self.cards) <= 0
    
    def showAllCards(self):
        print(self.name)
        print([[card.color, card.number] for card in self.cards])

    def getCard(self, cards):
        self.cards.extend(cards)

    def out(self):
        print(self.name, "没牌了，被淘汰出局")

    def win(self):
        print(self.name, "赢得了胜利")