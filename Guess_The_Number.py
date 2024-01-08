import random
import logoart
EASY_ATTEMPTS=10
HARD_ATTEMPTS=5
MEDIUM_ATTEMPTS=7  
def set_difficulty(level):
    if level=='easy':
        return EASY_ATTEMPTS
    elif level=='hard':
        return HARD_ATTEMPTS
    elif level=='medium':
        return MEDIUM_ATTEMPTS
    else:
        return 
def check_number(guessed_number,num,attempts):
    if guessed_number<num:
      print("Your guess is too low ")
      return attempts-1
    elif guessed_number>num:
      print("Your guess is too high ")
      return attempts-1
    else :
        print(f"Your guess is right.......The answer was {num} ")
        
def game():
            print(logoart.logo)
            print("Think of any number between 1 to 100 : ")
            num=random.randint(1,100)
            level=input("Chose the level : ")
            attempts=set_difficulty(level)
            if attempts!=EASY_ATTEMPTS and attempts!=MEDIUM_ATTEMPTS and attempts!=HARD_ATTEMPTS:
                print("You have entered wrong difficulty level....... Play again!")
                return
            guessed_number=0
            while (guessed_number!=num):
                print(f"You have {attempts} remaining to guess the number ")
                guessed_number=int(input("Guess the number : "))
                attempts=check_number(guessed_number,num,attempts)
                if attempts==0:
                    print("You are out of guess.....You lose!!")
                    return
                elif guessed_number!=num:
                    print("Guess again")
            
game()
