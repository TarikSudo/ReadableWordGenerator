import itertools
import string

def is_vowel(letter):
    return letter in 'aeiou'

def generate_readable_words(length=4): # Set the length
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))

    patterns = [
        (consonants, vowels, consonants, vowels),
        (vowels, consonants, vowels, consonants)
    ]

    readable_words = set()
    for pattern in patterns:
        for word in itertools.product(*[list(p) for p in pattern]):
            readable_words.add(''.join(word))

    return readable_words

four_letter_words = generate_readable_words(4)

# Save generated words to a CSV file
file_path = '/readable_words.csv'
with open(file_path, 'w') as file:
    for word in four_letter_words:
        file.write(word + '\n')

file_path
