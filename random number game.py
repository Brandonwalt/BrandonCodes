import random
import time

time_start = time.time()


def number_guessing_game(low, high):
    print("Guess a number between {low} and {high}. You have {rounds} rounds to try and guess correctly.".format(low=low, high=high))
    number = random.randint(low, high)

if __name__ == "__main__":
    timer = int(time.time() - time_start)
    guess = input("please enter a number : ")
    while timer <= 60 :
        try:  
            if timer >= 60:
                integer = int(guess)
                if integer == number:
                    print('Ya you won')
                    break
                elif integer < number:
                    print('Higher')
                elif integer > number:
                    print('Lower')
            else :
                break
        except ValueError:
            print("needs to be a number.")
    print("you were too slow, You lost.")


