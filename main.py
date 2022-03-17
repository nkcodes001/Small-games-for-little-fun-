import random
lst=["s","w","g"]

chances=10
no_of_chances=0
computer_point=0
human_point=0

print("___________________________________________________  Snake, Water, Gun>>>>> Game  ______________________________________________________________________________")

print(" s for SNAKE\n w for WATER \n G for GUN")

while no_of_chances<chances:
    _input=input("Snake,water or Gun:: ? : \t")
    _random=random.choice(lst)
   
    if(_random==_input):
       print("Tie---- Both Score 0 and 0 ")
       
    
    elif _input=="s" and _random=="w" :
        human_point=human_point+1
        print(f"Your guess: {_input} , Computer Guess: {_random}]\n")
        print("\n")
        print("Human Wins!,Whooooooooooooooooooooo!!!!!!\n")
        print(f"Computer Point is:  {computer_point}, Human point is : {human_point}")
        
    elif _input=="s" and _random=="g":
        computer_point=computer_point+1
        print(f"Your guess:  {_input} , Computer Guess: {_random}")
        print("\n")
        print("Computer Wins.... BOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!\n")
        print(f"Computer Point is:  {computer_point}, Human point is : {human_point}")   
        
        
    elif _input=="w" and _random=="s":
        computer_point=computer_point+1
        print(f"Your guess: {_input} , Computer Guess:  {_random}")
        print("\n")
        print("Computer Wins.... BOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!\n")
        print(f"Computer Point is: {computer_point}, Human point is : {human_point}")   
            
        
        
    elif _input=="w" and _random=="g":
        human_point=human_point+1
        print(f"Your guess: {_input} , Computer Guess: {_random}\n")
        print("\n")
        print("Human Wins!,Whooooooooooooooooooooo!!!!!!")
        print(f"Computer Point is:  {computer_point}, Human point is : {human_point}")    
        
    elif _input=="g" and _random=="s":
        human_point=human_point+1
        print(f"Your guess: {_input} , Computer Guess: {_random}\n")
        print("\n")
        print("Human Wins!,Whooooooooooooooooooooo!!!!!!")
        print(f"Computer Point is:  {computer_point}, Human point is : {human_point}")    
            
        
    elif _input=="g" and _random=="w":
        computer_point=computer_point+1
        print(f"Your guess: {_input} , Computer Guess: {_random}\n")
        print("\n")
        print("Computer Wins.... BOOOOOOOOOOOOOOOOOOOOOOOO!!!!!!!!!!!!!!!!\n")
        print(f"Computer Point is:  {computer_point}, Human point is : {human_point}")
        
        
    else:
        print("Wrong Input rey HOWLE!!!!!!!!!!!!!!\n")
        
    no_of_chances=no_of_chances+1
    print(f"{chances-no_of_chances}  left out of {chances} \n")
    
print("GAME OVER_______________________________________________________________________________________________________________________")

print("\nRESULTS--------------------------------------")
print("\n")

if(human_point==computer_point):
    print("Tie..................Better Luck next Time,,,,")
   
elif(computer_point>human_point):
    print("You LOOSE ........sorry for Your defeat")
    
elif(human_point>computer_point):
    print("Whoaaaaaa!!! You WINNNNNNN !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    

print(f"Your score :{human_point}  ,   Computer Score :{computer_point}")
 
print("_________________________________________________________________________________________________________________________________________")
    
    
    
    
    
        
        
        
