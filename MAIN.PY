import random
playing = True
number=str(random.randint(10,20))

print("i will generate a number from 10 to 20, and you have to guess the number one digit at a time.")
print("The game ends when you gett 1 hero!")

print("the game ends when you bast guess!")
while playing:
    guess = input("give me your best guess!\n")
    if number == guess:
        print("you win the game")
        print("the number was",number)
        break

    else:
        print("your guess isn't guite right, try again.\n")