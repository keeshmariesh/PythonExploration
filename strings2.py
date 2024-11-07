parrot = "Norwegian Blue"

print(parrot[0:6])  # Norweg
print(parrot[-14:-8])
print(parrot[-14:6])

print(parrot[0:6:2])    #Nre
print(parrot[0:6:3])    #Nw

number = "9,223;325:634 635,634;785"
separators = number[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print(parrot[-4:-2])    #Bl
print(parrot[-4:12])    #Bl

print(parrot[3:5])  # we
print(parrot[0:9])  # Norwegian
print(parrot[:9])   # Norwegian
print(parrot[10:14])# Blue
print(parrot[10:])  # Blue

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[0:9] + letters[9:18] + letters[18:27])

backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1]
print(backwards)

# Challenge - Use the letters string to do the following:
# Create a slice that produces the characters qpo.
# Slice the string to produce edcba.
# Slice the string to produce the last 8 characters, in reverse order.

#           01234567890123456789012345
#letters = "abcdefghijklmnopqrstuvwxyz"

print()
print(letters[16:13:-1])
print(letters[4:2:-1] + letters[2::-1])
print(letters[25:17:-1])