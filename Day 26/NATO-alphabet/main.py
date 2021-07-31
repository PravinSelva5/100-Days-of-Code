import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.DataFrame(data)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in nato_data_frame.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Please insert a word of your choice: \n").upper()
user_phonetic = [nato_dict[letter] for letter in user_input]

print(user_phonetic)