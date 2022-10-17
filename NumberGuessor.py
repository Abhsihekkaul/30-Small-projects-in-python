import random as rd

number = int(rd.randint(1,10))

guess = int(input("Guess the number : "))

if guess == number:
    print(f"Yay! you've successfully guessed the number {number}")
else:
    while guess != number:
        guess = int(input("Guess the number : "))
        if guess == number:
            print(f"Yay! you've successfully guessed the number {number}")
        elif guess > number:
            print("Too Big")
        elif guess < number:
            print("Too Short")
        else:
            print("You've Entered a wrong input")

        
