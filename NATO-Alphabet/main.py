import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

# make it to dictionary
dict_alphabet = {row.letter: row.code for (index, row) in df.iterrows()}
# user enter value
name = input("Enter a word: ")
name = name.upper().strip().replace(" ", "")
print(name)
# to make the list of the words
name_list = [dict_alphabet[letter] for letter in name]
print(name_list)
