# This program finds and returns the character that appears most frequently in a given string.
# If there is a tie for the most frequent character, return any of the characters with the highest frequency.
# Ignore spaces and count only alphabetic characters.
# The function should be case-insensitive.
# If the input is an empty string or only contains spaces, return None.

def most_frequent_char(text):
    # Step 1: Clean the text (remove spaces, make lowercase)
    cleaned_word = "".join(sorted(char.lower() for char in text if char != " "))
    # Step 2: Count character frequencies
    frequency = {}
    for char in cleaned_word:
        if char.isalpha():   #Ignore non-alphabetic characters
            char = char.lower() # Convert to lowercase
            if char in frequency:
                frequency[char] += 1    # Increment the count by 1
            else:
                frequency[char] = 1 # Add new character with count 1
    # Step 3: Find the character with the highest frequency
    max_count = 0
    max_chars = []
    for char in frequency:
        if frequency[char] > max_count:
            max_count = frequency[char]     # Set the new max_count
            max_chars = [char]              # Set the new char array
        elif frequency[char] == max_count:
            max_chars.append(char)          # Append to the end of the array
        else:
            continue
    return [max_chars, max_count]

# Prompt the user to enter text
print("Which character(s) have the highest frequency?")
print("Enter any text: ")
user_text = input()
# Call most_frequent_chars function on the user input text
most_frequent_chars = most_frequent_char(user_text)
# Clean the text
cleaned_text = ','.join(most_frequent_chars[0])
if len(most_frequent_chars[0]) > 1:
    print("The characters with the highest frequency are '" + cleaned_text + "'K and their frequency is " + str(most_frequent_chars[1]))
else:
    print("The character with the highest frequency is '" + cleaned_text+ "' and its frequency is " + str(most_frequent_chars[1]))
quit()