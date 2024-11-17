# Prompt the user for three integers separated by a comma (",")
# Return a + b - c

# prompt the user for the integers
integer_list = input("Please enter 3 integers (i.e. a,b,c): ").split(",")

# transform the string-type integer_list in to an int-type integer_list
for index in range(len(integer_list)):
    integer_list[index] = int(integer_list[index])

print(integer_list[0] + integer_list[1] - integer_list[2])

# # Demonstrating strings immutability
# tester = "Hello"
# # yields an error
# # tester[-1] = " "
# # you cannot assign the string "o" a new value of "
# # instead you must use a method or loop to assign a variation to a new var
# new_tester = tester.replace("o", " ")
# print(new_tester)
