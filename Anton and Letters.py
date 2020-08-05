letters = input()
letters = letters.replace('{', '')
letters = letters.replace('}', '')
letters = letters.replace(',', '')
letters = letters.replace(' ', '')

print(len(set(letters)))