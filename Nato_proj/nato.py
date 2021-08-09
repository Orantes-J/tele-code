import pandas as pd
STATEMENT = 'Insert a word: '
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

user_input = input(STATEMENT).upper()

# without comprehension
#
# split_word = []
# coded_nato = []
# for i in user_input:
#     split_word.append(i.upper())
# for letter in split_word:
#     for(index, rows) in nato_data.iterrows():
#         if letter == rows.letter:
#             coded_nato.append(rows.code)
#
# print(coded_nato)

phone_codes = { row.letter: row.code for (index, row) in nato_data.iterrows()}
output = [phone_codes[i] for i in user_input]

for i in user_input:
    print(f"{i} for " + phone_codes[i])