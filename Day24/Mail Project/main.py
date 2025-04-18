with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter_template = starting_letter.read()

with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

for name in names:
    name = name.strip()
    new_letter = letter_template.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        final_letter.write(new_letter)

