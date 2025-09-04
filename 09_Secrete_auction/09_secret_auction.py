import art_secret_bid
print(art_secret_bid.logo)
UserName = ""
bid = 0
highestBid = 0
newUser = "yes"
ContinueInput = True
storage_dict = {
}

# Get input from the user
def userInput():
    global UserName, bid
    UserName = input("What is your name: ")
    bid = int(input("Pleas write your bid: "))
    storage_dict[UserName] = bid

#Compare and find the highest bid
def compareBids():
    global highestBid
    for keys in storage_dict:
        if storage_dict[keys] > highestBid:
            highestBid = storage_dict[keys]
            winner = keys

    print(f"{winner} is the  winner, the bid was {highestBid}")
#Continue input from the player
while ContinueInput == True:
    userInput()
    newUser = input("Is there any player left ?\nWrite 'yes' or 'no' : ").lower()
    if newUser == "no":
        ContinueInput = False
    print("\n" * 100)
compareBids()
