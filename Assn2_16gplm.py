# Assignment 2, Friday February 15, 2018
# Gabrielle Mehltretter 20065730
# Creating two dice Game of Pig
# Human vs the computer
# The first player to accumulate a score of 100 wins

import random

def main() :

    playerScore = 0
    computerScore = 0
    turnNum = 0
    print("Welcome to the Game of Pig, the first player to reach a score of "\
    "100 wins.")
    print("You are player one. You roll first.")
    beginTurn = input("Press enter to start!")
    rollAgain = "y"
    playerTurnscore = 0
    computerTurnscore = 0

# The first while loop is to go through the turns of each player until one reaches a score of 100

    while playerScore < 100 and computerScore < 100 :
        turnNum = turnNum + 1
        playerScore = playerScore + playerTurnscore
        computerScore = computerScore + computerTurnscore
        print("It's turn number {}. Your score is {} and the computer's score is {}.".format(turnNum, playerScore, computerScore))
        playerTurnscore = 0
        computerTurnscore = 0
        
# the second while loop is for the players turn. This loop runs and goes through the conditionals
# until something is met in which case the player will go again or it will break the loop making
# it go to the computers turn

        while beginTurn == "" :
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            print("You rolled a {} and a {}".format(die1, die2))

# Conditionals for the dice roll


            if die1 != die2 :
                if die1 == 1 or die2 == 1 :
                    playerTurnscore = 0
                    print("Your turn is over.")
                    beginTurn = "computer"
                else :
                    playerTurnscore = playerTurnscore + (die1 + die2)
                    if playerScore + playerTurnscore >= 100 :
                        playerScore = playerScore + playerTurnscore
                        print("Congratulations, you won! The final score was {} for you and {} for the computer.".format(computerScore, playerScore))
                        break
                    
                    print("Your turn socre would be {} and your total game score would be {}".format(playerTurnscore, playerScore + playerTurnscore))
                    rollAgain = input("Would you like to roll again y/n?")
                    if rollAgain == "n" :
                        beginTurn = "computer"

                    
            elif die1 == die2 :
                if die1 == 1 == die2 :
                    playerTurnscore = playerTurnscore + 25
                    print("You rolled double ones, 25 has been added to your score. ")
                else :
                    playerTurnscore = playerTurnscore + 2 * (die1 + die2)
                    print("You rolled doubles, you must roll again.")

            if playerScore + playerTurnscore >= 100 :
                playerScore = playerScore + playerTurnscore
                print("Congratulations, you won! The final score was {} for the you and {} for the computer".format(computerScore, playerScore))
                break
                    
# Similar while loop to that of the players turn

        while beginTurn != "" :
            die3 = random.randint(1,6)
            die4 = random.randint(1,6)
            print("The computer rolled a {} and a {}".format(die3, die4))
            if die3 != die4 :
                if die3 == 1 or die4 == 1 :
                    computerTurnscore = 0
                    print("The computer's turn is over.")
                    beginTurn = input("Please press enter to continue ")
                else :
                    computerTurnscore = computerTurnscore + (die3 + die4)
                    if computerScore + computerTurnscore >= 100 :
                        computerScore = computerScore + computerTurnscore
                        print("The computer won! The final score was {} for the computer and {} for you.".format(computerScore, playerScore))
                        break
                    
# conditional to decide when the computer will stop rolling again. When the computer gets a score of 40
# or higher the computer will stop its turn
                    print("The computer's turn score would be {} and total game score would be {}".format(computerTurnscore, computerScore + computerTurnscore))
                    if computerTurnscore >= 40 :
                        beginTurn = input("Please press enter to continue.")


            elif die3 == die4 :
                if die3 == 1 == die4 :
                    computerTurnscore = computerTurnscore + 25
                    print("The computer rolled double ones, 25 has been added to the computer's score")
                else :
                    computerTurnscore = computerTurnscore + 2 * (die3 + die4)
                    print("The computer rolled doubles, The computer must roll again.")

            if computerScore + computerTurnscore >= 100 :
                computerScore = computerScore + computerTurnscore
                print("The computer won! The final score was {} for the computer and {} for you.".format(computerScore, playerScore))
                break
                

main()

        

