fafedgads
ga    global inBattle
    selectedMove = False
    if inBattle == True:
        print("""BReH MiMENT YrO'uE IN A BATtlE LmAo""")
    else:
        print("am fight")
        inBattle = True
        randomEnemy = random.randint(0, 3)
        target = enemies[randomEnemy]

        while inBattle == True:
            print(
                f"""YOUR TURN EPIC GA YMER \n YOUR TARGET IS A {target.name}! YOUR MOVES ARE:"""
            )
            print(moveMessage)
            while selectedMove == False:
                moveChoice = input("CHOOSE A MOVE: ")
                print(moveChoice)
                for i in range(0, len(moves)):
                    print("amogus")
                    print(moveChoice)
                    print(moves[i].name)
                    if str(moveChoice.lower) == str(moves[i].name):
                        print("kill")
                        randomAccuracy = random.randint(1, 100)
                        if randomAccuracy >= moves[i].accuracy:
                            #enemy attacks
                            print("lol you missed what a noob")
                            selectedMove = True
                        else:
                            damageDealt = random.randint(
                                moves[i].power, moves[i].power *
                                playerStats['attack']) / target.defence
                            target.health -= moves[i].power
                            #enemy attacks you
                            print(
                                f"""YOU {moves[i].name}ed THE {target}! YOU DEAL {damageDealt} DAMAGE! THE {target} NOW HAS {target.health} HP / {target.maxHealth} HP!"""
                            )
                            selectedMove = True
                    else:
                        #if the move isn't a move, keep repeating the if statement until its an actual move
                        print("select an actual move bozo")
                        selectedMove = False