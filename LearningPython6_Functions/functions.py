# Introduction to Python Functions

def multiply(x, y):
    result = x * y
    return result


def is_palindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    clean_string = ''.join(char for char in string
                           if char.isalnum())
    # return clean_string[::-1] == clean_string
    return is_palindrome(clean_string)


# 2 blank lines after each function definition is the convention
# Different examples of function calls below
# Uncomment to demonstrate different functions defined above
#
# answer = multiply(10.5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 6):
#     two_times = multiply(2, val)
#     print(two_times)
# Function call to check if a word is a palindrome
# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))
# Function call to check if any string is a palindrome
sentence = input("Please enter a sentence to check: ")
if palindrome_sentence(sentence):
    print("The sentence is a palindrome")
else:
    print("The sentence is not a palindrome")

