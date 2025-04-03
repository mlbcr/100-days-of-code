import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
dictionary = {row.letter: row.code for (index, row) in data.iterrows()}
print(dictionary)

word = input("Enter a word: ")
nano = [dictionary[letter.upper()] for letter in word]

print(nano)


