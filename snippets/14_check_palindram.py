str1 = "Kayak"
str2 = "kayak"

str1 = str1.upper()
str2 = str2.upper()

if str1 == str2[::-1]:
    print("True")
else:
    print("False")