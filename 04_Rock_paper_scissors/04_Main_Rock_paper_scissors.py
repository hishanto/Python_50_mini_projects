import random
import Ascii_art
print("Welcome To Rock Paper Scissors game\n")
player = int(input(" For Rock enter: 0\n For paper enter: 1\n For scissors enter: 2\n "))
ComputerAi = random.randint(0, 2)
if player == 0:
    print(" You Select Rock \n")
    print(Ascii_art.draw[player])
    print("\n\n AI Select  \n")
    print(Ascii_art.draw[ComputerAi])
elif player == 1:
    print(" You Select Paper \n")
    print(Ascii_art.draw[player])
    print("\n\n AI Select  \n")
    print(Ascii_art.draw[ComputerAi])
elif player == 2:
    print(" You Select Scissors \n")
    print(Ascii_art.draw[player])
    print("\n\n AI Select  \n")
    print(Ascii_art.draw[ComputerAi])
else:
    print("Wrong input")

if player == 0 and ComputerAi == 2:
    print("Scissors\nCongratulation You won")
elif player == 1 and ComputerAi == 0:
    print("Rock\nCongratulation You won")
elif player == 2 and ComputerAi == 1:
    print("Paper\nCongratulation You won")
elif player == ComputerAi :
    print("Its a draw, Try again!")
else:
    print("You Lose!!!")