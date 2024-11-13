computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse mat"
                  ]
print(computer_parts)

###### Different ways to mutate lists using built-in Python operators
# computer_parts[3] = "trackball"
print(computer_parts[3:])
# observe how these outputs differ
computer_parts[3:] = "trackball"
print(computer_parts)
computer_parts[3:] = ["trackball"]
print(computer_parts)

# for part in computer_parts:
#     print(part)
#
# print()
# print(computer_parts[2])
#
# print(computer_parts[0:3])