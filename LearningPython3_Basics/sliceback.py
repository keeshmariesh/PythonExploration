letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1] # Doesn't include 'a'
print(backwards)
backwards2 = letters[25::-1]    # Does include 'a'
print(backwards2)
backwards3 = letters[::-1]
print(backwards3)

# Challenge qpo edcba zyxwvut
print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

print(letters[-4:])
print(letters[-1:])
print(letters[:1])