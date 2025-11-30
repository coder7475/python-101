# Importing Regular Expressions Library
import re

name = 'Python is 1'

digits = re.sub("[^0-9]", "", name)
letters = re.sub("[^a-zA-Z]", "", name)
spaces = re.findall("[ \n]", name)

# print(digits)
print(len(digits))
# print(letters)
print(len(letters))
# print(spaces)
print(len(spaces))

print("----------------------")
# Another approach
digitsCount  = sum(c.isdigit() for c in name)
lettersCount = sum(c.isalpha() for c in name)
spacesCount  = sum(c.isspace() for c in name)

print(digitsCount)   # 1
print(lettersCount)  # 8
print(spacesCount)   # 2
