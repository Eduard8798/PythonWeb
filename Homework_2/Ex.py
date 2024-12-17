from itertools import count

WorldBasketball = [
    {"name": "Карим Абдул-Джаббар", "height": 218},
    {"name": "Майкл Джордан", "height": 198},
    {"name": "Леброн Джеймс", "height": 206},
    {"name": "Коби Брайант", "height": 198}
]

def addPlayer(player):
    name = input('enter  name: ')
    height = int(input('enter  height: '))
    player.append({"name": name, "height": height})
    print('player added')
    printPlayer(WorldBasketball)

def printPlayer(playerList):
    for player in playerList:
        print(player)

def deletePlayer(playerList):
        namePlayer = input('enter  name for delete: ')
        for name in playerList:
            if name["name"] != namePlayer:
                 print('player not found')
            else:
                playerList.remove(name)
                return
        print('player deleted')
        printPlayer(WorldBasketball)

def editPlayer(playerList):
    name = input('enter  name: ')
    height = int(input('enter  height: '))
    for player in playerList:
        if player["name"] == name:
            height = player["height"]
            player["name"] = input("enter  name: ")
            player["height"] = int(input("enter  height: "))
        else:
            print('player not found')
    printPlayer(WorldBasketball)



print('Switch to use functions \n 1 - addPlayer \n 2 - deletePlayer \n 3 - editPlayer')
count = int(input('enter  number: '))

if  count == 1:
    printPlayer(WorldBasketball)
    addPlayer(WorldBasketball)
if count == 2:
    printPlayer(WorldBasketball)
    deletePlayer(WorldBasketball)
if count == 3:
    printPlayer(WorldBasketball)
    editPlayer(WorldBasketball)
else:
    print('Error number')



