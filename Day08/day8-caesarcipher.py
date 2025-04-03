import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
answer = 'yes'
while answer != 'no':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        for letter in start_text:
            if letter in alphabet:
                if cipher_direction == 'encode':
                    position = alphabet.index(letter) + shift_amount
                    end_text += alphabet[position]
                elif cipher_direction == 'decode':
                    position = alphabet.index(letter) - shift_amount
                    end_text += alphabet[position]
            else:
                end_text += letter
        print(f"The {direction}d text is {end_text}")

    shift = shift % 26

    caesar(text, shift, direction)
    answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    print()
print('Goodbye')