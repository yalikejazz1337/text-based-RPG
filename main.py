#import required libraries
import random
import math

#define variables
playerStats = {
    'health': 100,
    'maxHealth': 100,
    'defence': 10,
    'attack': 10,
    'coins': 100,
    'level': 1,
    'exp': 0,
    'bank': 0
}


def allNumeric(string):
    if(len(string) == 0):
      return False
    for i in string:
        if i.isdigit() == False:
          return False
    return True


class moveClass:
    def __init__(self, name, power, accuracy):
        self.name = name
        self.power = power
        self.accuracy = accuracy


#move

stab = moveClass('stab', 7, 90)
fireball = moveClass('fireball', 10, 85)
bow = moveClass("bow", 11, 75)
glock = moveClass('glock-69', 10, 60)
amogus = moveClass('amogus', 8, 69)

moves = [stab, fireball, bow, glock, amogus]

moveMessage = ""

for i in range(len(moves)):
    moveMessage += str(i + 1) + ": " + (
        moves[i].name).upper() + " Power: " + str(
            moves[i].power) + " Accuracy: " + str(moves[i].accuracy) + "\n"

moveMessage += "Use the number next to the move name to use that move!"

commands = ['help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank']
bankCommands = ['deposit', 'withdraw']

allCommands = [
    'help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank', 'deposit',
    'withdraw'
]

maxHealth = playerStats['maxHealth']
level = playerStats['level']
xpBonus = 1 + playerStats['bank']/1000 * level
bank = playerStats['bank']
purse = playerStats['coins']
inBattle = False

#boss class


class bossClass:
    def __init__(self, name, attack, defence, health, maxHealth):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxHealth = maxHealth


#bossClass

boss1 = bossClass('The Sus', 100, 100, 100, 100)


def levelUp():
    xp = playerStats['exp']
    xpRequire = 1000 * (pow(1.25, level))
    if xp >= xpRequire:
        playerStats['maxHealth'] += 25
        playerStats['level'] += 1
        playerStats['attack'] += 5
        playerStats['defence'] += 5
        playerStats['exp'] = 0
        print(
            'good job you leveled up'
        )


class enemyClass:
    def __init__(self, name, attack, defence, health, maxHealth):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxHealth = maxHealth

    def resetEnemy(self, health, maxHealth):
        self.health = self.maxHealth


#enemies

zombie = enemyClass('Zombie', 10, 10, 100, 100)
skeleton = enemyClass('Skeleton', 15, 5, 90, 90)
spider = enemyClass('Spider', 10, 15, 95, 95)

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
               Exit: Exits the game.
               """

#healing


def heal():
    coins = playerStats['coins']
    price = 25
    bank = playerStats['bank']
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
    xpBonus = 1 + playerStats['bank']/1000 * level
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


#define kill


def killZombie():
    zombie.health = zombie.maxHealth


def killSkeleton():
    skeleton.health = skeleton.maxHealth


def killSpider():
    spider.health = spider.maxHealth


#level system
#hunt function


def hunt():
    global inBattle
    if inBattle == True:
        print(
            "you're in a battle bozo- even if i'd let you 2v1 you'd automatically die"
        )
    elif inBattle == False:
        inBattle = True
        enemy = random.randrange(0, 3, 1)
        target = enemies[enemy]
        print(f"You are battling a {target.name}!")
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
                        if(target.health > 0):
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
                            die()
                            inBattle = False
                            return "l bozo"
                            
                if (not (moveChoice.isnumeric()
                         and int(moveChoice) <= len(moves))):
                    print("select an actual move bozo")
                if target.health <= 0:
                    xpEarned = round(random.randrange(100, 750, 10) * xpBonus)
                    coinsEarned = random.randrange(100, 375, 10)
                    playerStats['coins'] += coinsEarned
                    playerStats['exp'] += xpEarned
                    print(
                        f"good job you killed the {target.name} and earned {coinsEarned} coins and {xpEarned} xp"
                    )
                    target.health = target.maxHealth
                    levelUp()
                    inBattle = False


def die():
    xpLost = random.randint(100 * level, 500 * level)
    coinsLost = random.randint(10, 50)
    if(coinsLost >= playerStats['coins']):
      coinsLost = playerStats['coins']
    if(xpLost >= playerStats['exp']):
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
          Health: {round(health)} / {maxHealth}
          Attack: {attack}
          Defence: {defence}
          Coins in Purse: {coins}
          Coins in Bank: {bank}
          Level: {level}
          XP: {math.floor(xp)} / {math.floor(1000*pow(1.25, level))}
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
            break

        if playerStats['health'] <= 0:
            die()

        if command == commands[0]:
            print(helpCommand)

        if command == commands[1]:
            hunt()

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
