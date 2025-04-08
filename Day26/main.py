import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(dictionary)

def generate_phonetic():
    word = input("Enter a word: ")
    try:
        nano = [dictionary[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(nano)

generate_phonetic()

