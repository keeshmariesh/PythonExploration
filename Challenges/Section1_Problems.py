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

    print("String: " + char_string)
    print("The case-insensitive duplicate characters are as follows: ")
    for index, char in enumerate(dup_list):
        print("'{}': {}".format(char, num_list[index]))


# #2 Find the first non-repeated character: Write a program that returns
# the first non-repeated character from a given string.

def first_non_repeat(string):
    

count_dup_chars("hello world D L O")

