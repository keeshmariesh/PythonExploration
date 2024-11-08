# This program takes in two strings and checks if they are anagrams
def string_slicer(slicer):
    # This function slices the string into its lowercase letters
    # Declare a reference variable string
    newSlice = ""
    for char in slicer:
        if(char == " "):
            continue # Skip to the next character in the string if its an empty space
        else:
            newSlice = newSlice + char.lower()
    newArray = sorted(newSlice)
    newSlice = "".join(newArray)
    return newSlice

# Take in two words
print("The 1st word is: ")
word1 = string_slicer(input())
print("The 2nd word is: ")
word2 = string_slicer(input())

#Check if the words are identical
if(word1 == word2):
    print("The words are INDEED anagrams!!!")
    quit()
else:
    print("The words are NOT anagrams!!!")
    quit()