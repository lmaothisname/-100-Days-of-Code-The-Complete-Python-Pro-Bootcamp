import pandas
nato_read = pandas.read_csv(r"D:\Python\Day 26\nato_phonetic_alphabet.csv")
nato_data = pandas.DataFrame(nato_read)
nato_phonetic = {row.letter:row.code for (index,row) in nato_data.iterrows()}
name = input("Enter a word: ").upper()
show = [nato_phonetic[letter] for letter in name]
print(show)