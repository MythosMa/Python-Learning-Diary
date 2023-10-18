# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

n = int(input("请输入玩家数量："))
players = []
currentNum = 1
playerIndex = 0
for i in range(n):
    players.append(i + 1)

while len(players) > 1:
    print(f"{players[playerIndex]}->{currentNum}")
    if currentNum == 3:
        currentNum = 1
        players.pop(playerIndex)
    else:
        currentNum += 1
        playerIndex += 1
        
    if playerIndex >= len(players):
        playerIndex = 0

print(players[0])