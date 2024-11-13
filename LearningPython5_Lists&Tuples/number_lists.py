even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
empty_list = []

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = sorted("432985617")
print(digits)

even_more_digits = sorted("342345151546")
print(even_more_digits)

# a few ways to do the same thing below
# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers)
print(numbers == more_numbers)


### Uncomment various code snippets below to observe various Python functionality
# # Extend method. Adds an iterable to the end of the iterable being acted upon
# even.extend(odd)
# print(even)
# another_even = even
# print(another_even)
# # Sort method. Sorts a sequence in place. Mutates it.
# even.sort(reverse=True)
# print(even)
# print(another_even)

# min & max methods
# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# #len method
# print()
# print(len(even))
# print(len(odd))
#
# #count method
# print()
# print("mississippi".count("s"))
# print("mississippi".count("iss"))

