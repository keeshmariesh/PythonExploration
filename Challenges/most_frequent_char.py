# This program finds and returns the character that appears most frequently in a given string.
# If there is a tie for the most frequent character, return any of the characters with the highest frequency.
# Ignore spaces and count only alphabetic characters.
# The function should be case-insensitive.
# If the input is an empty string or only contains spaces, return None.

def most_frequent_char(text):
    # Step 1: Clean the text (remove spaces, make lowercase, keep only alphabetic characters)
    cleaned_text = [char.lower() for char in text if char.isalpha()]

    # Step 2: Count character frequencies
    frequency = {}
    for char in cleaned_text:
        frequency[char] = frequency.get(char, 0) + 1  # Increment count, defaulting to 0 if char is new

    # Step 3: Find the character(s) with the highest frequency
    max_count = max(frequency.values(), default=0)
    max_chars = [char for char, count in frequency.items() if count == max_count]

    # Step 4: Return results
    return max_chars, max_count

# Prompt the user to enter text
print("Which character(s) have the highest frequency?")
user_text = input("Enter any text: ")

# Call the function
most_frequent_chars, frequency = most_frequent_char(user_text)

# Format the output
if most_frequent_chars:
    if len(most_frequent_chars) > 1:
        print(f"The characters with the highest frequency are '{', '.join(most_frequent_chars)}' with a frequency of {frequency}.")
    else:
        print(f"The character with the highest frequency is '{most_frequent_chars[0]}' with a frequency of {frequency}.")
else:
    print("No alphabetic characters found.")