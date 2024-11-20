##### Chapter 1 Problems #####

# #1 Counting duplicate characters: Write a program that counts duplicate
# characters from a given string.

def count_dup_chars(char_string):
    """Prints the duplicate characters in a given string."""
    lower_case = char_string.lower()
    unique_list = list(set("".join(lower_case.split())))
    dup_list = []
    num_list = []

    for char in unique_list:
        if lower_case.count(char) == 1:
            continue
        dup_list += [char]
        num_list += [str(lower_case.count(char))]

    for index, char in enumerate(dup_list):
        print("'{}': {}".format(char, num_list[index]))


# #2 Find the first non-repeated character: Write a program that returns
# the first non-repeated character from a given string.

def first_non_repeat(string):
    """Returns the first non-repeated character from a string."""
    unique_list = list(set(string))
    index = 0

    for i, char in enumerate(string):
        if i == 0:
            if char == string[i + 1]:
                continue
            else:
                return char
        elif i == len(string) - 1:
            print("No repeating characters.")
            break
        elif string[i-1] != string[i] and string[i + 1] != string[i]:
            index = i
            return string[i]


# #3 Reversing letters and words: Write a program that reverses that
# letters of each word and a program that reverses the letters of each
# the words themselves.

def letter_reverse(string):
    """Returns a string with the letters in each word reversed."""
    return " ".join(word[::-1] for word in string.split())


def letter_word_reverse(string):
    """Returns a string with the letters and words reversed."""
    return " ".join(word[::-1] for word in string.split()[::-1])


# #4 Check whether a string contains only digits: Write a program that
# checks whether the given string contains only digits. The String class
# method: isdigit()

# #5 Counting vowels and consonants: Write a program that counts the
# number of vowels and consonants in a given string. Do this for the
# English language, which has five vowels (a, e, i, o, and u).

def count_vow_cons(string):
    """Returns the number of a vowels and consonants in the string."""
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_num = 0
    consonant_num = 0

    for char in string:
        if not char.isalpha():
            continue
        elif char.lower() in vowels:
            vowel_num += 1
            continue
        consonant_num += 1
    return vowel_num, consonant_num


# #6 Count occurrences of a character in a string: Write a program that
# counts the occurrences of a certain character in a given string.
# The String class method: count()

# #7 Convert String into int or float: Write a program that converts the
# given String object (representing a number) into int or float.

def string_int_converter(string):
    """Converts a string into an int."""
    return int(string)


def string_float_converter(string):
    """Converts a string into a float."""
    return float(string)


# #8 Removing whitespaces from a string: Write a program that removes all
# white spaces from the given string.

def remove_whitespaces(string):
    """Returns a string with all of the whitespaces removed."""
    return string.replace(" ", "")

# #9 Joining multiple strings with a delimiter: Write a program that
# joins the given strings by the given delimiter.

def concatenate_strings(delimiter, *args):
    """Returns a given set of strings joined by a given delimiter."""
    return delimiter.join(args)


# #10 Generate all permutations: Write a program that generates all
# the permutations of a given string.




# #1
print("Problem #1:\n")
count_dup_chars("hello world D L O")
print()

# #2
print("Problem #2:\n")
print(first_non_repeat("SSSkRRRttttlllllleeeee"))
print()

# #3
print("Problem #3:\n")
print(letter_reverse("Hello World"))
print(letter_word_reverse("Hello World"))
print()

# #4
print("Problem #4:\n")
print("223123123".isdigit())
print("324kd342s".isdigit())
print()

# #5
print("Problem #5:\n")
print(count_vow_cons("How many vowels and consonants in this string?"))
print()

# #6
print("Problem #6:\n")
print("How many i's are in this string?".count("i"))
print()

# #7
print("Problem #7:\n")
integer, floating = string_int_converter("15"), string_float_converter("15.75")
print("Integer: {}\nFloat: {}".format(integer, floating))
print()

# #8
print("Problem #8:\n")
print(remove_whitespaces("This string should not have any whitespaces"))
print()

# #9
print("Problem #9:\n")
print(concatenate_strings("+", "Here", "is", "a",
                          "concatenated", "string!"))

# #10
