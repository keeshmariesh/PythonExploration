# Two approaches in this code to print out all the meals in the menu,
# but with the "spam" removed.
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
##### Method 1
# Remove spam from each list, then print the list
# for menu_list in menu:
#     top_index = len(menu_list) - 1
#     for index, item in enumerate(reversed(menu_list)):
#         if item == "spam":
#             del menu_list[top_index - index]
#     print(menu_list)
#
# print()
# print("*" * 80)
# print()

##### Method 2
# Print out the items in each list, as long as it's not spam
# for menu_list in menu:
#     new_list = []
#     for item in menu_list:
#         if item != "spam":
#             new_list += [item]
#     print(new_list)
#
# print()
# print("*" * 80)
# print()
##### Method 3
# More on the print() function. Use end to avoid newline
# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item, end=", ")
#     print()
##### Method 4
# Using join

for meal in menu:
    for index in range(len(meal) - 1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(", ".join(meal))



