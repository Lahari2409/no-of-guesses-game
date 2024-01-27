import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():#random.randint(4) "123" or "srihari"
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)#(randint(1,4))--1,2,3,4


guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:#3>2
        print("You were above the number!")
    else:#1>2
        print("You were below the number!")

print("You got it in", guesses, "guesses")
