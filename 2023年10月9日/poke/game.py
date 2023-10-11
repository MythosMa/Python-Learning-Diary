from card import Card
from player import Player
import random

pool = []

players = [Player("刘德华"), Player("张学友"), Player("郭富城"), Player("黎明")]
random.shuffle(players)

cards = [Card(color, number) for color in ["方片", "梅花", "红桃" , "黑桃"] for number in range(1, 14)]
random.shuffle(cards)

while len(cards) > 0:
    for player in players:
        player.deal(cards.pop())

def roundPlay(player: Player):
    global pool
    print("当前牌池:", [[card.color, card.number] for card in pool])
    playCard = player.play()
    for index, card in enumerate(pool):
        if(card.number == playCard.number):
            getCard = pool[index:]
            pool = pool[:index]
            getCard.append(playCard)
            player.getCard(getCard)
            return
    pool.append(playCard)

playersCount = len(players)
while playersCount > 1:
    for player in players:
        if player.checkIsNoCards() == False:
            roundPlay(player)
            if player.checkIsNoCards():
                player.out()
                playersCount -= 1
        if playersCount <= 1:
            break
    
for player in players:
    if player.checkIsNoCards() == False:
        player.win()
        break

# roundPlay(players[0])
# print([[card.color, card.number] for card in cards])