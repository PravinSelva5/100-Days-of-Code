from art import logo 

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    
    for char in text:
        if char in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"Here's the {direction}d result: {end_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift, direction)

    result = input("Type 'yes' if you want to go again, Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("GoodBye")