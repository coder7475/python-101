numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]

for num in numberList:
    if num > maxNum:
        maxNum = num
    
print(maxNum)
# Using built in function
print(max(numberList))