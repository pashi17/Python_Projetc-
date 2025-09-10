import random

target=random.randint(1,100)

while True:
    userChoice = input("Guess the target :- ")
    if(userChoice == "Quit"):
        break

    userChoice =int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess :- ")
        break
    elif(userChoice < target):
        print("Your no is Too Small. Take a bigger Guess :-  ")
    else:
        print("Your number was too big. Take a smaller guess...")

print("Game Over.........")
       