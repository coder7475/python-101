str1 = "Listen"
str2 = "Silent"


str1 = list(str1.lower())
str2 = list(str2.lower())

str1.sort()
str2.sort()

# print(str1)
# print(str2)

if str1 == str2:
    print("True")
else:
    print("False")