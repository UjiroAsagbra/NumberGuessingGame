import random
import time
print("Guess a number between 1 and 50")
time.sleep(1)
guess = int(input("Guess the number: "))

Correct_Number = random.randint(1,50)
guess_count = 1

while guess != Correct_Number:
        guess_count += 1

        if Correct_Number > guess:
                print("Wrong answer. Guess higher")
        else:
                print("Wrong answer. Guess lower")

        guess = int(input("Guess the number: "))


print(f"Congrats! The right answer is {Correct_Number}. It took you {guess_count} guesses.")

