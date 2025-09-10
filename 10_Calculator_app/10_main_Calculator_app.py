def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply (n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
loopContinue = True
while loopContinue:
    firstVar = int(input("Enter the 1st Number: "))
    for symbol in operations:
        print(symbol + "\n")
    userIn = input("Enter the operation you want to execute: ")
    lastVar = int(input("Enter the 2nd Number: "))
    result = operations[userIn](firstVar, lastVar)
    print(f"{firstVar} {userIn} {lastVar} = {result}")

    again = input("Still need to calculate ?\n 'Yes' or 'No' " ).lower()
    if again != "yes":
        loopContinue = False
