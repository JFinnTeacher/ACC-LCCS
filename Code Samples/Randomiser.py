import random

def random_uppercase(word):
    # Randomly change some letters to uppercase
    new_word = ''.join([char.upper() if random.choice([True, False]) else char for char in word])
    return new_word

def replace_e_with_3(word):
    # Randomly change letter 'e' to '3'
    new_word = ''.join([random.choice(['3', 'e']) if char == 'e' else char for char in word])
    return new_word

def replace_s_with_dollar(word):
    # Randomly change letter 's' to '$'
    new_word = ''.join([random.choice(['$', 's']) if char == 's' else char for char in word])
    return new_word

def transform_word(word):
    # Step 1: Randomly change some letters to uppercase
    word = random_uppercase(word)
    
    # Step 2: Randomly change 'e' to '3'
    word = replace_e_with_3(word)
    
    # Step 3: Randomly change 's' to '$'
    word = replace_s_with_dollar(word)
    
    return word

# Input from user
input_word = input("Enter a word: ")

# Transform the word
transformed_word = transform_word(input_word)

# Output the transformed word
print("Transformed word:", transformed_word)