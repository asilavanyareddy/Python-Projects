import random
number=random.randint(1,100)
guesses=0
limit=10
print("Welcome To Number Guessing Game")
print("Instrtuctions:")
print("you should guess a number between 1 to 100")
print("You have 10 chances to guess the number correctly")
while guesses<limit:
    usernumber=int(input("enter the number you guess : "))
    guesses+=1
    remaining=limit-guesses
    if(usernumber==number):
        print(f"you have guessed the number correctly in {guesses} guesses.Congratulations!")
        break
    elif(usernumber>number):
        print("the number you entered is too high")
        print(f"oops!you only have {remaining} guesses now")
    else:
        print("the number you entered is too low")
        print(f"oops!you only have {remaining} guesses now")
        if(remaining==0):
            print("End of the Game")
playagain=input(print("do you want to play again: (yes/no)"))
if playagain!="yes":
    print("Thanks for playing!")



