import re
spChar = "!@#$%^&*()"

count = re.sub(r'[\w]+', '', spChar)
print(len(count))   # 10
