# Introduction to Python Functions

def multiply(x, y):
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence. If you pass
    a string, for example, as the first argument, you'll get
    the string repeated 'y' times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    return x * y


def is_palindrome(string):
    """
    Check if a sentence is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(string):
    """
    Get a string argument by passing a value.

    The function ignores whitespace, capitalisation, and
    punctuation in the sentence.

    :param string: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    clean_string = ''.join(char for char in string
                           if char.isalnum())
    return is_palindrome(clean_string)


def fibonacci(n):
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


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
# sentence = input("Please enter a sentence to check: ")
# if palindrome_sentence(sentence):
#     print("The sentence is a palindrome")
# else:
#     print("The sentence is not a palindrome")

# Print documentation; Docstrings
# answer = multiply(18, 3)
# print(answer)
#
# print(multiply.__doc__)
# print(is_palindrome.__doc__)
# print(palindrome_sentence.__doc__)

for i in range(36):
    print(i, fibonacci(i))
