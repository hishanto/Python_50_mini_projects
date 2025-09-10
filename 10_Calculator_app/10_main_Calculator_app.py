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
firstVar = int(input("Enter the 1st Number: "))
userIn = input("Enter the operation you want to execute")
lastVar = int(input("Enter the 2nd Number: "))
result = operations[userIn](firstVar, lastVar)
print(result)