from replit import clear
from art import logo


def add(a, b):
  return a+b

def subtract (a,b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a,b):
  return a/b

op={"+": add,
"-": subtract,
"*": multiply,
"/":divide}

def calc():
  print(logo)
  for n in op:
    print(n)
  n1=float(input("What's the first number? "))
  should_continue=True
  while should_continue:
    n2=float(input("What's the next number? "))
    sym=input("Pick an operation from the line above: ")
    fun=op[sym]
    ans=fun(n1, n2)
    print(f"{n1} {sym} {n2} = {ans}")
    c=input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation.: ")
    if c=='y':
      n1=ans
    else:
      should_continue=False
      calc()

calc()
