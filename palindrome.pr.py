def is_palindrome(word):
    # Remove any spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is the same forwards and backwards
    return word == word[::-1]

# Ask the user to enter a word
word = input("Enter a word: ")

# Check if the word is a palindrome and print the result
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")