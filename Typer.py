import random,time
score = 0
try:
    while True:
        with open(".\\Lib\\coins.css","r") as file:
            coins = file.read()
            with open(".\\Lib\\data.css","r") as file:
                highscore = file.read()
        go = input("Typer  V1.0  HighScore:" + str(highscore) + " Coins:" + coins + "[GO]")
        if go == 'go' or 'Go':
            while True:
                start = time.time()
                randomnum = str(random.randint(0,10))
                RAM = input('[' + str(score) + ']' + randomnum + '> ')
                end = time.time()
                if end - start < 1:
                    if RAM == randomnum:
                        score += 1
                        continue
                    else:
                        print("GameOver!")
                        break
                else:
                    print("GameOver!")
                    break
        if score < int(highscore):
            print("Your score:" + str(score) + ",Highscore:" + highscore + ".You have take " + str(score * 50) + ".")
            print("get once!")
            coins = int(coins) + score * 50
            with open(".\\Lib\\coins.css","w") as file:
                file.write(str(coins))
                continue
        elif score > int(highscore):
            print("Your score:" + str(score) + ",Highscore" + str(score) + "YOU TAKE THE HIGHSCORE!You have take " + str(score*50 + 100) + '.') 
            print("get once!")
            coins = int(coins) + score * 50 + 100
            with open(".\\Lib\\coins.css","w") as file:
                file.write(str(coins))
                with open(".\\Lib\\data.css",'w') as file:
                    file.write(str(score))
                    continue

        else:
            print("Your score:" + str(score) + ",Highscore:" + highscore + ".Just a little wrong!.You have take " + str(score * 50) + ".")
            print("get once!")
            coins = int(coins) + score * 50
            with open(".\\Lib\\coins.css","w") as file:
                file.write(str(coins))
                continue
except Exception:
    pass




    
