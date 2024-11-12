#This program counts the number of duplicate characters in a string

string1 = input("Please enter a string: ")
chars = {}

for char in string1:
    if char.isalpha():
        chars[char.lower()] = chars.get(char.lower(), 0) + 1

print()

for char in chars:
    if chars[char] > 1:
        print("'{}': {}".format(char, chars[char]))