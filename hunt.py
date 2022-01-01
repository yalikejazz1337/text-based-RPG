def hunt() 
 
 enemyHunted = random.randint(1, 4)

    if enemyHunted == 1:

        enemyHunted = zombie
        damageTaken = random.randint(enemyHunted.attack, 5 * enemyHunted.attack)
        damageTaken = damageTaken / playerStats['defence']
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25, 100)
        xpEarned = random.randint(100 * xpBonus, 500 * xpBonus)

        if playerStats['health'] <= 0:
            die()

        elif enemyHunted.health <= 0:
            playerStats['coins'] += coinsEarned
            playerStats['exp'] += xpEarned
            print(
                f"""You killed a zombie and earned {coinsEarned} coins. You also earned {xpEarned} XP."""
            )
            killZombie()

        else:
            print("""You weren't able to defeat the zombie and ran away.""")
        

    if enemyHunted == 2:
        enemyHunted = skeleton
        damageTaken = random.randint(enemyHunted.attack,
                                     5 * enemyHunted.attack)
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25, 100)
        xpEarned = random.randint(100, 500)

        if playerStats['health'] <= 0:
            die()

        elif enemyHunted.health <= 0:
            playerStats['coins'] += coinsEarned
            playerStats['exp'] += xpEarned
            print(
                f"""You killed a skeleton and earned {coinsEarned} coins. You also earned {xpEarned} XP"""
            )
            killSkeleton()

        else:
            print("""You weren't able to defeat the skeleton and ran away.""")

    if enemyHunted == 3:
        enemyHunted = spider
        damageTaken = random.randint(enemyHunted.attack,
                                     5 * enemyHunted.attack)
        damage = random.randint(playerStats['attack'], 25)
        enemyHunted.health -= damage
        playerStats['health'] -= damageTaken
        coinsEarned = random.randint(25, 100)
        xpEarned = random.randint(100, 500)

        if playerStats['health'] <= 0:
            die()

        elif enemyHunted.health <= 0:
            playerStats['coins'] += coinsEarned
            playerStats['exp'] += xpEarned
            print(
                f"""You killed a spider and earned {coinsEarned} coins. You also earned {xpEarned} XP"""
            )
            killSpider()

        else:
            print("""You weren't able to defeat the spider and ran away.""")