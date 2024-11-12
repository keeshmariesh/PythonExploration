# Write a program that returns the first non-repeated character

phrase = input("Please input a string: ")

for i, char in enumerate(phrase):
    if phrase[i-1] != char and char != phrase[i+1]:
        print(char)
        break
