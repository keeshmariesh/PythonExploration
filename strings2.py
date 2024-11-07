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

letters = "abcdefghijklmnopqrstuvwxyz"

print(letters[0:9] + letters[9:18] + letters[18:27])


