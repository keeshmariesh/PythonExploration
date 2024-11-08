# This program takes in two strings and checks if they are anagrams
def prepare_string(word):
    # Convert to lowercase and remove spaces
    cleaned_word = "".join(sorted(char.lower() for char in word if char != " "))
    return cleaned_word

def are_anagrams(word1, word2):
    # Check if the processed versions of both words are identical
    return prepare_string(word1) == prepare_string(word2)

# Take input from the user
word1 = input("Enter the 1st word: ")
word2 = input("Enter the 2nd word: ")

# Check if the words are anagrams and print the result
if are_anagrams(word1, word2):
    print("The words are INDEED anagrams!!!")
else:
    print("The words are NOT anagrams!!!")
