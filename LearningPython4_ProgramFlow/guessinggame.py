import random

# # The following are different prototypes testing out Python fundamentals
# while loop

highest = 1000
answer = random.randint(1, highest)
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))
while guess != answer:
    guess = int(input())

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


# highest = 10
# answer = random.randint(1,highest)
# print(answer)   # TODO: Remove after testing
#
# print("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
#
# if guess == answer:
#     print("You got it the first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
#         print(answer)

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")
# else:
#     print("You got it first time")
