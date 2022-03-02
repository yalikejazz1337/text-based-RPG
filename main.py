#import required libraries
import random
import math
import json
#define variables

with open('save.json', 'r') as openfile:
    json_object = json.load(openfile)

with open('save2.json', 'r') as openfile:
    json_object2 = json.load(openfile)

with open('save3.json', 'r') as openfile:
    moveList = json.load(openfile)




playerStats = json_object

playerItems = json_object2

bossBattled = False 


def allNumeric(string):
    if (len(string) == 0):
        return False
    for i in string:
        if i.isdigit() == False:
            return False
    return True


class moveClass:
    def __init__(self, name, power, accuracy, moveId):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.moveId = moveId


#move


stab = moveClass('stab', 7, 90,0)
fireball = moveClass('fireball', 10, 85,1)
bow = moveClass("bow", 11, 75,2)
glock = moveClass('glock-69', 10, 60,3)
amogus = moveClass('amogus', 8, 69,4)
ak_47 = moveClass('AK-47', 15, 50,5)
crossbow = moveClass('Crossbow', 13, 60,6)

allMoves = [stab, fireball, bow, glock, amogus, ak_47, crossbow]
moves = []

for i in moveList:
  thing = i
  moves.append(allMoves[moveList[thing]])

def makeMoveMessage():
  global moveMessage
  moveMessage = ""
  for i in range(len(moves)):
    moveMessage += str(i + 1) + ": " + (moves[i].name).upper() + " Power: " + str(moves[i].power) + " Accuracy: " + str(moves[i].accuracy) + "\n"
  moveMessage += "Use the number next to the move name to use that move!"
makeMoveMessage()

commands = ['help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank']
bankCommands = ['deposit', 'withdraw']
#The sus is a filler boss because yes. Then battle leviathan thingy and if win == treu then captain is ded and yeah. Battle ded captain becuz he mad he ded. Win
#then bsatttle impostoser becasuxe he sez he;s the captain back 2 liyf. Win. 


allCommands = [
    'help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank', 'deposit',
    'withdraw', 'shop', 'buy', 'sell'
]

shopCommands = ['shop', 'buy', 'sell']

maxHealth = playerStats['maxHealth']
xpBonus = 1 + playerStats['bank'] / 1000 * playerStats['level'] + 1
bank = playerStats['bank']
purse = playerStats['coins']
inBattle = False

#shop
class armorClass:
  def __init__(self, name, defence, levelReq, price):
    self.name = name
    self.defence = defence
    self.levelReq = levelReq
    self.price = price
    self.type = "armour"

class swordClass:
  def __init__(self, name, att, levelReq, price):
    self.name = name
    self.att = att
    self.levelReq = levelReq
    self.price = price
    self.type = "sword"

basicArmor = armorClass("Basic-Armor", 5, 1, 0)
woodArmor = armorClass('Wooden-Armor', 7.5, 1, 100)


armours = [basicArmor]


basicSword = swordClass("Basic-Sword", 5, 1, 0)
woodSword = swordClass('Wooden-Sword', 7.5, 1, 100)

swords = [basicSword, woodSword]


class moveItemClass:
    def __init__(self, name, price, move):
        self.name = name
        self.price = price
        self.move = move
        self.type = "move"

class itemClass:
    def __init__(self, name, price, item):
        self.name = name
        self.price = price
        self.item = item
        self.type = "item"
        self.defence = "placeholder"
        self.att = "placeholder" 


AK_47 = moveItemClass('AK-47', 700, ak_47)
Crossbow = moveItemClass('Crossbow', 600, crossbow)




itemList = [AK_47, Crossbow]

for i in range(0, len(armours)):
  itemList.append(itemClass(armours[i].name, armours[i].price, armours[i]))

for i in range(0, len(swords)):
  itemList.append(itemClass(swords[i].name, swords[i].price, swords[i]))

shopMessage = ''


def shop():
    global shopMessage

    for i in range(0, len(itemList)):
        if(itemList[i].type == "move"):
          shopMessage += f"""
                                  -------{itemList[i].name}------\n
                                  PRICE: {itemList[i].price}\n
                                  POWER: {itemList[i].move.power}\n
                                  ACCURACY: {itemList[i].move.accuracy} \n
    """
        elif(itemList[i].type == "item" and itemList[i].item.type == "sword"):
            shopMessage += f"""
                                  -------{itemList[i].name}------\n
                                  PRICE: {itemList[i].price}\n
                                  ATT: {itemList[i].att}\n
    """
        elif(itemList[i].type == "item" and itemList[i].item.type == "armour"):
            shopMessage += f"""
                                  -------{itemList[i].name}------\n
                                  PRICE: {itemList[i].price}\n
                                  DEF: {itemList[i].defence}\n
    """
    print(shopMessage)

    selectingItem = True

    while selectingItem == True:
        selectingItem = True
        itemChoice = input("select an item to buy: ")
        if itemChoice == 'exit':
            return 'bozo left shop'
        if (allNumeric(itemChoice)):
            if (int(itemChoice) >= 0 and int(itemChoice) <= len(itemList)):
                
                selectingItem = False
                #valid thing
        if(selectingItem == True):
          print("select an actual item bozo")
    if playerStats['coins'] < itemList[int(itemChoice)-1].price:
        print("don't have enough coins lmao")
    else:
        if(itemList[itemChoice].type == "move"):
          global moves
          selectingReplacement = True
          while selectingReplacement:
            joe = input("select the move you want to overwrite \n" + moveMessage + ': ')
            if(allNumeric(joe)):
              selectingReplacement = False
            else:
              print("type a number idot")
              selectingReplacement = True
        elif(itemList[int(itemChoice)-1].type == "item"):
            confirming = True
            while confirming == True:
              confirm = input('are you sure you want to replace your ' + playerItems[itemList[int(itemChoice)-1].item.type] + " with " + itemList[int(itemChoice)-1] + "(1 if yes and 0 if no)")
              if(allNumeric(confirm)):
                if(int(confirm) == 1 or int(confirm) == 0):
                  confirming = False
                else:
                  print("you typed a number that isn't 1 or 0")
              else:
                print("only the numbers 0 and 1 please")
            if(confirm == 0):
              print("SHOPKEEPER: next time come in and actually buy something")
              return "angered shopkeeper ending"
            elif(confirm == 1):
              playerItems['armour'] = itemList[int(itemChoice)-1]
              print("Successfully replaced " + playerItems[itemList[int(itemChoice)-1].item.type] + "with " + itemList[int(itemChoice)-1])
            

        moves[int(joe)-1] = (itemList[int(itemChoice)-1].move)
        playerStats['coins'] -= itemList[int(itemChoice)-1].price
        print(
            f"""Successfully purchased {itemList[int(itemChoice)-1].name} for {itemList[int(itemChoice)-1].price} coins!""")
        makeMoveMessage()
        return 'amogus'


#boss class


class bossClass:
    def __init__(self, name, attack, defence, health, maxHealth, xpYield):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxHealth = maxHealth
        self.xpYield = xpYield
        self.type = "boss"


#bossClass

boss1 = bossClass('Sus', 10, 10, 250, 250, 1000)
boss2 = bossClass('Leviathon', 15, 30, 375, 375, 2000)
boss3 = bossClass('Crew Captian', 17, 20, 300, 300, 4500)
boss4 = bossClass('Impostor', 22, 10, 500, 500, 7500)


bosses = [boss1, boss2, boss3, boss4]




def levelUp():
    xp = playerStats['exp']
    xpRequire = 1000 * (pow(1.25, playerStats['level']))
    if xp >= xpRequire:
        playerStats['maxHealth'] += 25
        playerStats['level'] += 1
        playerStats['attack'] += 5
        playerStats['defence'] += 5
        playerStats['exp'] = 0
        playerStats['bossBattled'] = 0
        


class enemyClass:
    def __init__(self, name, attack, defence, health, maxHealth, xpYield):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxHealth = maxHealth
        self.type = "enemy"
        self.xpYield = xpYield

    def resetEnemy(self, health, maxHealth):
        self.health = self.maxHealth


#enemies

zombie = enemyClass('Zombie', 10, 10, 100, 100, 250)
skeleton = enemyClass('Skeleton', 15, 5, 90, 90, 250)
spider = enemyClass('Spider', 10, 15, 95, 95, 250)

enemies = [zombie, skeleton, spider]
#enemies for later levels/areas
enemies2 = []

#help list
helpCommand = """
               --------------------------
               List of available commands:
               --------------------------
               Help: Displays this page.
               --------------------------
               Hunt: Go hunting.
               --------------------------
               Shop: Look at available shop items.
               --------------------------
               Heal: Heals you to full health for the cost of 25 coins.
               --------------------------
               Boss: Takes you to the ULTRA-OMEGA-EPIC-CRAZY-BOSS (UOECB)
               --------------------------
               Stats: Displays statistics such as coins, health, defence, and attack.
               --------------------------
               Bank: Displays how many coins you have in your purse and
               how many coins you have in your bank and other help with banks.
               -------------------------
               quit: Quits the game.
               """

#healing


def heal():
    coins = playerStats['coins']
    price = 25
    bank = playerStats['bank']
    if playerStats['health'] == playerStats['maxHealth']:
        print('You have full health bozo')
        return 'bozo had full health'
    else:
        if coins < price and bank > price:
            print(
                f"""You only have {coins} in your purse. Withdraw some from your bank to buy this item."""
            )
        elif coins < price and bank < price:
            print(
                f"""You don't have enough money to buy this. You have {coins}, but you need {price}."""
            )
        else:
            if coins >= price:
                playerStats['health'] = maxHealth
                print("Restored to full health!")
                playerStats['coins'] -= price


#banking
def bank():
    coins = playerStats['coins']
    inBank = playerStats['bank']
    xpBonus = 1 + playerStats['bank'] / 1000 * playerStats['level']
    print(f"""
          --------------------------
                  YOUR BANK
          --------------------------
          Your purse: {coins}
          In bank: {inBank}
          --------------------------
          XP Bonus: {xpBonus}x more XP.
          --------------------------
          To Withdraw, use withdraw (amount).
          To deposit, use deposit (amount).
          You can also use 'all' which will deposit
          all coins in purse or withdraw all coins from bank.
          --------------------------
          """)


def deposit():
    amount = input('Enter the amount you would like to deposit: ')

    if amount == 'all':
        playerStats['bank'] += playerStats['coins']
        playerStats['coins'] -= playerStats['coins']
        print("""Successfully deposited all coins!""")

    else:
        amount = int(amount)
        if playerStats['coins'] < amount:
            print(
                """Cannot deposit that much; you don't have enough in your purse!"""
            )
        else:
            playerStats['coins'] -= amount
            playerStats['bank'] += amount
            print(f"""Successfully deposited {amount} coins.""")


def withdraw():
    withdrawAmount = input('Enter the amount you would like to withdraw:')

    if withdrawAmount == 'all':
        playerStats['coins'] += playerStats['bank']
        playerStats['bank'] -= playerStats['bank']
        print("""Successfully withdrew all coins!""")
    else:
        withdrawAmount = int(withdrawAmount)
        if playerStats['bank'] < withdrawAmount:
            print("""That's too much to withdraw!""")
        else:
            playerStats['bank'] -= withdrawAmount
            playerStats['coins'] += withdrawAmount
            print(f"""Successfully withdrew {withdrawAmount} coins!""")

#level system
#hunt function


def hunt(targetE):
    global inBattle
    global moveMessage
    if inBattle == True:
        print(
            "you're in a battle bozo- even if i'd let you 2v1 you'd automatically die"
        )
    elif inBattle == False:
        inBattle = True
        target = targetE
        if(target.type == "enemy"):
          print(f"You are battling a {target.name}!")
        elif(target.type == "boss"):
          print(f"You are battling the {target.name}!!")
        while inBattle == True:
            print("Your moves are: \n" + moveMessage)
            moveSelected = False
            while moveSelected == False:
                moveChoice = input(f"""Choose a move: """)
                if allNumeric(moveChoice) == False:
                    print("don't use anything but numbers pls thanks")
                    moveSelected = False
                else:
                    moveSelected = True
            for i in range(0, len(moves)):
                if (int(moveChoice) == i + 1):
                    randomAccuracy = random.randrange(0, 100, 1)
                    if randomAccuracy >= moves[i].accuracy:
                        #miss
                        print('l bozo you missed')
                        enemyDamage = round(
                            (random.randrange(10, 25, 1) / 10) *
                            target.attack *
                            (1 - playerStats['defence'] / 2000))
                        playerStats['health'] -= enemyDamage
                        if playerStats['health'] <= 0:
                            die()
                            inBattle = False
                            return "l bozo"
                        else:
                            print(
                                f"the {target.name} did {enemyDamage} damage to you- ouch you now have {playerStats['health']} hp / {playerStats['maxHealth']} hp"
                            )
                    else:
                        #attack with that move's accuracy and power
                        #after attack enemy, enemy attacks you and then it repeats
                        damageDealt = round(
                            (random.randrange(10, 60, 1) / 10) *
                            (moves[i].power * playerStats['attack'] / 10) *
                            (1 - target.defence / 2000))
                        target.health -= damageDealt
                        if (target.health > 0):
                            print(
                                f"You attacked the {target.name} and did {damageDealt} damage to the enemy! The {target.name} now has {target.health} hp / {target.maxHealth} hp!"
                            )

                            enemyDamage = round(
                                (random.randrange(10, 25, 1) / 10) *
                                target.attack *
                                (1 - playerStats['defence'] / 2000))

                            playerStats['health'] -= enemyDamage
                            print(
                                f"the {target.name} did {enemyDamage} damage to you- ouch you now have {playerStats['health']} hp / {playerStats['maxHealth']} hp"
                            )
                        if playerStats['health'] <= 0:
                            target.health = target.maxHealth
                            die()
                            inBattle = False
                            return "l bozo"

                if (not (moveChoice.isnumeric() and int(moveChoice) <= len(moves))):
                    print("select an actual move bozo")
                if target.health <= 0:
                    if(target.type == "enemy"):
                        target.health = target.maxHealth
                        
                        inBattle = False
                        xpEarned = round(random.randrange(target.xpYield, target.xpYield + 250, 10) * xpBonus)
                    elif(target.type == "boss"):
                        xpEarned = round(random.randrange(target.xpYield, target.xpYield + 1000, 10) * xpBonus)
                        playerStats['currentBoss'] += 1
                        inBattle = False
                    coinsEarned = random.randrange(100, 375, 10)
                    playerStats['coins'] += coinsEarned
                    if(xpEarned < 1000 * pow(1.25,playerStats['level'])):
                      playerStats['exp'] += xpEarned
                      print(
                        f"good job you killed the {target.name} and earned {coinsEarned} coins and {xpEarned} xp"
                      )
                    else:
                      levelsGained = 0
                      while xpEarned > 1000 * pow(1.25,playerStats['level']):
                        xpEarned -= 1000 * pow(1.25,playerStats['level'])
                        playerStats['exp'] += 1000 * pow(1.25,playerStats['level'])
                        levelUp()
                        levelsGained += 1
                      xpEarned += 1000 * pow(1.25,playerStats['level'])
                      print(
                        f"good job you killed the {target.name} and earned {coinsEarned} and levelled up {str(levelsGained).upper()} time(s)! "
                      )
                    
                    
                    
                    break


def die():
    xpLost = random.randint(100 * playerStats['level'], 500 * playerStats['level'])
    coinsLost = random.randint(10, 50)
    if (coinsLost >= playerStats['coins']):
        coinsLost = playerStats['coins']
    if (xpLost >= playerStats['exp']):
        xpLost = playerStats['exp']
    print(f'You died and lost {coinsLost} coins. You also lost {xpLost} XP. ')
    playerStats['health'] = 100 * playerStats['level']
    playerStats['exp'] -= xpLost
    playerStats['coins'] -= coinsLost

    

#stats


def stats():
    health = playerStats['health']
    attack = playerStats['attack']
    defence = playerStats['defence']
    coins = playerStats['coins']
    level = playerStats['level']
    xp = playerStats['exp']
    bank = playerStats['bank']

    print(f"""
          -----------------------------------------
                      PLAYER STATISTICS
          -----------------------------------------
          Health: {round(health)} / {playerStats['maxHealth']}
          Attack: {attack}
          Defence: {defence}
          Coins in Purse: {coins}
          Coins in Bank: {bank}
          Level: {level}
          XP: {math.floor(xp)} / {math.floor(1000*pow(1.25, level))}
          Armor: {playerItems['armor']}
          Sword: {playerItems['sword']}
          -----------------------------------------
          """)


#game loop

while True:

    command = input("""Enter a command. Enter 'Help' for list of commands: """)

    if command not in allCommands:
        print("""
              ------------------------------------------------------------
              Woah there. That command doesn't exist. Try 'help' for help.
              ------------------------------------------------------------
              """)

    if command in commands or bankCommands:
        if command == commands[-2]:
            print('Quitting.....')
            json_object = json.dumps(playerStats, indent=8)

            with open("save.json", "w") as outfile:
                outfile.write(json_object)

            json_object2 = json.dumps(playerItems, indent=2)

            with open("save2.json", "w") as outfile:
                outfile.write(json_object2)
            
            moveList = {"move1" :moves[0].moveId, "move2" :moves[1].moveId,  "move3" :moves[2].moveId,  "move4" :moves[3].moveId,  "move5" :moves[4].moveId}



            json_object3 = json.dumps(moveList, indent=5)    
            with open("save3.json", "w") as outfile:
                outfile.write(json_object3)
        
            break


        if playerStats['health'] <= 0:
            die()

        if command == commands[0]:
            print(helpCommand)

        if command == commands[1]:
          enemy = random.randrange(0, 3, 1)
          EnemyTarget = enemies[enemy]
          hunt(EnemyTarget)
          
        if command == commands[-3]:
            stats()

        if command == commands[-1]:
            bank()

        if command == bankCommands[0]:
            deposit()

        if command == commands[3]:
            heal()

        if command == bankCommands[1]:
            withdraw()

        if command == shopCommands[0]:
            shop()

        if command == commands[4]:
          bossTarget = bosses[playerStats['currentBoss']]
          hunt(bossTarget)
            