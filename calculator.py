import sys
import os
import time

def ani(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def clear_screen():
    ani('--------------------------------------------------------')
    time.sleep(20)
    # Check the operating system and run the appropriate clear command
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS and Linux
        os.system('clear')

f = 0
t = 0
e = 0
operator = 0

def calculator(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "/":
            return a/b
        elif op == "*":
            return a*b
        else:
            return None
    except:
        return None

ani("Which operator will you be using?: ")    
operator = input("")
if operator not in ["+","-","/","*"]:
    ani("INVALID - REASON: NOT AN OPERATOR LISTED, RESTART CONSOLE")
    clear_screen()

try:
    ani("What is the first number you will be using the operator on? ")
    f = int(input(""))
    ani("What is the second number you will be using on the first? ")
    t = int(input(""))
except:
    ani("INVALID - REASON: NOT A NUMBER, RESTART CONSOLE")
    clear_screen()

e = calculator(f, t, operator)
if e == None:
    print("The answer is undefined")
if e != None:
    print("The answer is", e)
clear_screen()
