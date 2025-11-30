import decimal

integer = 10

print(type(integer))
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

string = '1234'

print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))
