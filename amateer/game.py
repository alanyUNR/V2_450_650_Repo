# Dice game

import random
import sys

print("BEAT THE HOUSE")
print("--------------")
print("Roll higher than the house to win!")
uInput = input("How many other players are there?\n")

try:
    intInput = int(uInput)
except:
    print("We can only play if you enter an integer. Goodbye.")
    sys.exit(1)

if intInput > 10:
    print("Too many players. Goodbye")
    sys.exit(1)


numPlayers = int(uInput) + 1
playerList = []
scoreDict = {}

print("")

for player in range(numPlayers):
    playerList.append(f"Player #{player + 1}")
    scoreDict[f"Player #{player + 1}"] = 0

numRounds = numPlayers * 1
rerollAvailable = True

for round in range(numRounds):
    print(f"Round {round+1}")
    dRollOne = random.randint(1, 6)
    dRollTwo = random.randint(1, 6)
    dRollCombo = dRollOne + dRollTwo
    print(f"The house rolled: {dRollOne} + {dRollTwo} = {dRollCombo}")
    for player in playerList:
        pRollOne = random.randint(1, 6)
        pRollTwo = random.randint(1, 6)
        pRollCombo = pRollOne + pRollTwo
        print(f"{player} rolled: {pRollOne} + {pRollTwo} = {pRollCombo}")
        if player == "Player #1" and rerollAvailable:
            while True:
                rerollChoice = input(
                    "Choose a die to reroll (1 or 2), or enter k to keep: "
                ).strip().lower()
                if rerollChoice in ("1", "2", "k"):
                    break
                print("Please enter 1, 2, or k.")

            if rerollChoice == "1":
                pRollOne = random.randint(1, 6)
                rerollAvailable = False
            elif rerollChoice == "2":
                pRollTwo = random.randint(1, 6)
                rerollAvailable = False

            pRollCombo = pRollOne + pRollTwo
            print(f"{player}'s final roll: {pRollOne} + {pRollTwo} = {pRollCombo}")

        if pRollCombo > dRollCombo:
            scoreDict[player] += 1
    print("")

finalScores = dict(
    sorted(scoreDict.items(), key=lambda item: item[1], reverse=True))

print("Final Results")
for k, v in finalScores.items():
    print(f"{k}: {v}")

p1Position = list(finalScores.keys()).index("Player #1")
print("")
print(f"You finished #{p1Position+1} in the game.")

if p1Position + 1 == 1:
    print("Well done, you won!")
else:
    print("Bad luck, try again.")