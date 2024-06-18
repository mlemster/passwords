import random
import secrets
import string

# List of random words to use in the password
word_list = [
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew', 'kiwi',
    'lemon', 'mango', 'nectarine', 'orange', 'papaya', 'quince', 'raspberry', 'strawberry',
    'tangerine', 'ugli', 'vanilla', 'watermelon', 'xigua', 'yam', 'zucchini'
]

# List of special characters to include in the password
special_chars = string.punctuation


# Function to generate the password
def generate_password(num_words=4, num_specials=2):
    # Select random words
    words = [secrets.choice(word_list) for _ in range(num_words)]

    # Select random special characters
    specials = [secrets.choice(special_chars) for _ in range(num_specials)]

    # Combine the words and special characters
    password_list = words + specials

    # Shuffle the password list to mix words and special characters
    random.shuffle(password_list)

    # Combine the list into a single string
    password = ''.join(password_list)

    return password


# Generate a password
password = generate_password()
print("Generated password:", password)
