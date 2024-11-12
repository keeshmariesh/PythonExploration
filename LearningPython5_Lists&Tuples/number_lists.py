#Operations you can perform with mutable sequence types
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Extend method. Adds an iterable to the end of the iterable being acted upon
even.extend(odd)
print(even)
another_even = even
print(another_even)
# Sort method. Sorts a sequence in place. Mutates it.
even.sort(reverse=True)
print(even)
print(another_even)

# #min & max methods
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

