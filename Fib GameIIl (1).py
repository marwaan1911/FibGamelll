import random
coinsLeft = random.randint(2, 30)
coinsToRemove = 0
userTurn = True

print("This is a game where players take turns taking coins from a pile of coins. The player who takes the last coin wins. The current coin count is: ", coinsLeft)
while coinsLeft > 0:
    while userTurn == True and coinsLeft > 0:

        coinsToRemove = int(input("How many coins do you want to remove?"))

        if coinsToRemove > 3:
            print("you can't remove more than three coins at a time! The current stone count is: " + str(coinsLeft))

        elif coinsLeft - coinsToRemove < 0:
            print("There aren't that many coins left!")

        else:
            coinsLeft -= coinsToRemove
            print("The First Player removed " + str(coinsToRemove) + " coin(s)! The current coin count is: " + str(coinsLeft))


            userTurn = False
    while userTurn  == False and coinsLeft > 0:

     coinsToRemove = int(input("How many coins do you want to remove?"))
     coinsLeft -= coinsToRemove
     if coinsToRemove > 3:
         print("you can't remove more than three coins at a time! The current stone count is: " + str(coinsLeft))

     print( "The Second Player removed " + str(coinsToRemove) + "coin(s)! The current coin count is: " + str(coinsLeft))


     userTurn = True
        
        
        
    

if userTurn == True:
    print("The Second Player took the last coin, it win. You lost the game!")

else:
    print("You took the last coin, you win. The Second Player lost the game!")
