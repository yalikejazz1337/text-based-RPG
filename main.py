#import required libraries
import numpy as np
from numpy import random

#define variables
playerStats = {'health': 100, 'defence': 10, 'attack': 10, 'coins': 100, 'level': 1, 'exp': 100, 'bank': 1}

commands = ['help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank']
bankCommands = ['deposit', 'withdraw']

allCommands = ['help', 'hunt', 'shop', 'heal', 'boss', 'stats', 'quit', 'bank', 'deposit', 'withdraw']

maxHealth = playerStats['health'] * playerStats['level'] 
level = playerStats['level']
xpBonus = playerStats['bank'] / 10

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




#banking
def bank():
    coins = playerStats['coins']
    inBank = playerStats['bank']

    
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
          You can also use all which will deposit
          all coins in purse or withdraw all coins from bank.
          --------------------------
          """)
    
    
def deposit():
    purse = playerStats['coins']
    bank = playerStats['bank']
    
    amount = int(input('Enter the amount you would like to deposit: '))
    
    playerStats['coins'] -= amount
    playerStats['bank'] += amount
    
    
    

#define kill 

def killZombie():
    zombie.health = zombie.maxHealth
    
def killSkeleton():
    skeleton.health = skeleton.maxHealth
    
def killSpider():
    spider.health = spider.maxHealth
    
#hunt function

def hunt():
    enemyHunted = random.randint(1,4)
   
    if enemyHunted == 1:
        
        enemyHunted = zombie
        damageTaken = random.randint(enemyHunted.attack, 25)
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage 
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25,100)
        xpEarned = random.randint(100 * xpBonus,500 * xpBonus)
        
            
        if playerStats['health'] <= 0:
            die()
            
        elif enemyHunted.health <= 0:
                playerStats['coins'] += coinsEarned
                playerStats['exp'] += xpEarned
                print(f"""You killed a zombie and earned {coinsEarned} coins. You also earned {xpEarned} XP.""")
                killZombie()
            
        else:
            print("""You weren't able to defeat the zombie and ran away.""")
            
        
        
    if enemyHunted == 2:
        enemyHunted = skeleton
        damageTaken = random.randint(enemyHunted.attack, 25)
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage 
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25,100)
        xpEarned = random.randint(100,500)
        
            
        if playerStats['health'] <= 0:
            die()
            
        elif enemyHunted.health <= 0:
                playerStats['coins'] += coinsEarned
                playerStats['exp'] += xpEarned
                print(f"""You killed a skeleton and earned {coinsEarned} coins. You also earned {xpEarned} XP""")
                killSkeleton()
            
        else:
            print("""You weren't able to defeat the skeleton and ran away.""")
            
   
    if enemyHunted == 3:
        enemyHunted = spider
        damageTaken = random.randint(enemyHunted.attack, 25)
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage 
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25,100)
        xpEarned = random.randint(100,500)
        
            
        if playerStats['health'] <= 0:
            die()
            
        elif enemyHunted.health <= 0:
                playerStats['coins'] += coinsEarned
                playerStats['exp'] += xpEarned
                print(f"""You killed a spider and earned {coinsEarned} coins. You also earned {xpEarned} XP""")
                killSpider()
            
        else:
            print("""You weren't able to defeat the spider and ran away.""")
            
        

#death

def die():
    xpLost = random.randint(100 * level, 500 * level)
    coinsLost = random.randint(10,50)
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
          Health: {health} / {maxHealth}
          Attack: {attack}
          Defence: {defence}
          Coins in Purse: {coins}
          Coins in Bank: {bank}
          Level: {level}
          XP: {xp}
          -----------------------------------------
          """)

#enemy class

class enemyClass:
    def __init__(self, name, attack, defence, health, maxHealth):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.health = health
        self.maxHealth = maxHealth

#enemies

zombie = enemyClass('Zombie', 10, 10, 10, 10)
skeleton = enemyClass('Skeleton', 15, 5, 10, 10)
spider = enemyClass('Spider', 10, 15, 10, 10)

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
            
            
            
            
    
            