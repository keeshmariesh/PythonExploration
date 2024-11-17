# Tuples

# different ways to declare and assign tuples

# t = "a", "b", "c"
# print(t)
#
# t = ("a", "b", "c")
# print(t)

# # print by indexing the tuple
welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

### You can't execute the line below because tuples are immutable
# metallica[0] = "Master of Puppets"

### Coerce the tuple into a list. Now its mutable...
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# # other ways to unpack tuple
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
#
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length*width)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1984),
          ]

# print(len(albums))

# Ways to unpack tuples from a list
for album in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(album[0], album[1], album[2]))
# another way to unpack a tuple from a list
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))


