f = 0
t = 0
e = 0
operator =0

def calculator(a, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "/":
        return a/b
    elif operator == "*":
        return a*b
    else:
        print("INVALID FORMAT")
    
operator = input("Which operator will you be using?: ")

f = int(input("What is the first number you will be using the operator on? "))
t = int(input("What is the second number you will be using on the first with the operator? "))

e = calculator(f, t)
print(e)
