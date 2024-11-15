# Prompt the user for three integers separated by a comma (",")
# Return a + b - c

# prompt the user for the integers
integer_list = input("Please enter 3 integers (i.e. a,b,c): ").split(",")

# transform the string-type integer_list in to an int-type integer_list
for index in range(len(integer_list)):
    integer_list[index] = int(integer_list[index])

print(integer_list[0] + integer_list[1] - integer_list[2])

