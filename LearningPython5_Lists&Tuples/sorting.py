pangram = "The quick brown fox jumps over the lazy dog"

# sorted() method takes an iterable and it returns a sorted list
letters = sorted(pangram)
print(letters)
# sorted() leaves the original list unchanged
numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
# sort() method modifies list in place and returns None
numbers.sort()
print(numbers)

# key=str.casefold forces sorted() to ignore case when sorting
missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)


names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)

# sort() method modifies list in place and returns None
# another_sorted_numbers = numbers.sort() - assigns the value None to var
# print(numbers)
# print(another_sorted_numbers) - this would return None