import random


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = get_integer(": ")

    if guess == answer:
        print("Well done, you've guessed it")
        break
    elif guess == 0:
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
