import random
def guess_num(attempts:int):
    num : int =random.randint(1,50)
    while attempts > 0:
        guess = int(input("Guess the number between 1 to 50: "))
        attempts-=1
        if num > guess:
            print(f"Your guess {guess} is too low. Guess again you have {attempts} left")
            
        elif num<guess:
            print(f"Your guess {guess} is too high. \nGuess again you have {attempts} left")
        else :
            print(f"Your guess {guess} is correct")
            break
        
        if attempts == 0:
            print(f"Sorry, you've run out of attempts. The correct number was {num}.")
            break

                
def main():
    print(""" \t*Guess The Number Game* """)
    level = int(input("Whats your level \n1.Easy \n2.Hard \n"))
    if level == 1:
        print("You have 10 attempts to guess the number")
        attempts=10
        guess_num(attempts)
    else:
        print("you have 5 attempts to guess the number")
        attempts=5
        guess_num(attempts)
main()
