import random
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
print("You have 7 tries to guess the number.Good Luck!!!\n")
number = random.randint(1,100)
tries = 7
while tries >0:
    try:
        guess = int(input("Take a guess: "))
        if guess < 1 or guess > 100:
            print("Please guess a number between the range limit")
            continue
        if guess < number:
            print("The number is too low!!!")
            
        elif guess > number:
            print("The number is too high!!!")
        else:
            print("You got it!!! Great Job!!!")
            break
        tries-= 1
        if tries > 0:
            print("You have ", tries, "tries left\n")
        else:
            print("You have run out of tries!!! The number was ", number)
            
    except ValueError:
        print("Please enter a valid number")                         