PLACEHOLDER = "[name]"

# read invited names
with open("./Input/Names/invited_names.txt")as names_file:
    names = names_file.readlines()
    # print(names)
# open the letter and read
with open("./Input/Letters/letter.txt") as letter_file:
    letter_contents = letter_file.read()
    # to replace
    for name in names:
        new_invited_letter = letter_contents.replace(PLACEHOLDER, name.strip())
        # print(new_invited_letter)
        # write the new file
        with open(f"./Output/letter_for_{name.strip()}.txt", mode="w") as letter_done:
            letter_done.write(new_invited_letter)
