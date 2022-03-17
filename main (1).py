import random

correctNum=random.uniform(1,100)
theNum=int(correctNum)


noOfGuesses=1


while(noOfGuesses<=9):
    print("Enter your guess:",end="\t")
    guess=int(input())
    
    
    if guess==theNum:
        print("WHoooooooo,U got the correct guess")
        break
    elif guess<theNum:
        print("Enter greater NumbEr please!!    ")
        
    else :
        print("enter lesser no. please")
    
    print("No. of Guesses left=",9-noOfGuesses)
    noOfGuesses=noOfGuesses+1
    
if noOfGuesses>9:
    print("No more chances left,Better luck next time")
    



