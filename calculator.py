import math
while True:
  num1=int(input("enter 1st number: "))
  num2=int(input("enter 2nd number: "))
  sign=input("select (+,-,*,/) one operation: ")
  match sign:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)
    case _:
        print("invalid")
  calculate_again=input("do you want to calculate again: (yes/no)? ")
  if(calculate_again=="no"):
    print("Thanks for using")
    break

    