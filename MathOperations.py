x = (str(input("Enter a math symbol: ")))

if x == "+":
    def add(num1, num2):
        additon = num1 + num2
        print(additon)
    add(56, 78)
elif x == "-":
    def subtract(num1, num2):
        subtraction = num1 - num2
        print(subtraction)
    subtract(1, 2)
elif x == "*":
    def multiply(num1, num2):
        multiplication = num1 * num2
        print(multiplication)
    multiply(786, 786)
elif x == "/":
    def divide(num1, num2):
        division = num1 / num2
        print(division)
    divide(908, 982)
