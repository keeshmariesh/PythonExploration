# Tuple Practice Exercises - Uncomment the code to demonstrate

# Tuple Custom Sort by Second Element in the List
#
# data =(("Alice", 88), ("Bob", 92), ("Charlie", 85), ("Diana", 90))
#
# def get_second_element(item):
#     return item[1]
#
# tuple_list = sorted(data, key = get_second_element)
#
# print(tuple_list)

# Tuple Manipulation with Indexing
#
# employees = (
#         ("Alice", "Engineering", 85000),
#         ("Bob", "Marketing", 65000),
#         ("Charlie", "Engineering", 90000),
#         ("Diana", "HR", 55000)
#     )
# # Extract high earners
# high_earners = [employee for (employee, dept, salary) in employees if salary > 80000]
#
# # Create a tuple of unique departments, sorted alphabetically
# departments = sorted(tuple(set(department for (employee, department, salary) in employees)))
#
# print("High Earners: {}\nDepartments: {}".format(high_earners, departments))

# Tuple Group by Starting Letter
#
# names = ("Alice", "Andrew", "Bob", "Charlie", "Catherine", "Brian")
#
# first_letters = sorted(list(set(name[0] for name in names)))
#
# tuple_list = [
#     (first_letter, list(new_name for new_name in names if new_name[0] == first_letter))
#     for first_letter in first_letters
# ]
#
# print(tuple_list)

# Tuple Transformation and Filtering
#
# people = [("Alice", 30), ("Bob", 40), ("Charlie", 100), ("Diana", 98)]
#
# modified_people = list((name, age + 5) for (name, age) in people if age + 5 <= 100)
#
# print(modified_people)

# Tuple with Even and Odd Numbers
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# evens = tuple(number for number in numbers if number % 2 == 0)
# odds = tuple(number for number in numbers if number % 2 != 0)
#
# print(evens)
# print(odds)

# Tuple of Word Lengths
#
# words = input("Please enter a sentence devoid of punctuation: ").split()
#
# word_tuple = tuple((word, len(word)) for word in words)
#
# print(word_tuple)

