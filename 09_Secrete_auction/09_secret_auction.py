import art_secret_bid
print(art_secret_bid.logo)
UserName = ""
bid = 0
newUser = "yes"
ContinueInput = True
storage_dict = {
}

# Get input from the user
def userInput():
    UserName = input("What is your name: ")
    bid = int(input("Pleas write your bid: "))
    storage_dict[UserName] = bid

#Continue input from the player
while ContinueInput == True:
    userInput()
    newUser = input("Is there any player left ?\nWrite 'yes' or 'no' : ").lower()
    print("\n" * 100)
    if newUser == "no":
        ContinueInput = False
