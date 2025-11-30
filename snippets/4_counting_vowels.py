vowels = ['a', 'e', 'i', 'o', 'u']

word = 'programming'

count = 0

for char in word:
    if char in vowels:
        count += 1

print(count)