fib = [0, 1]

for i in range(5):
    fib.append(fib[-1] + fib[-2])

print('List: ', fib)

# Converting list of integers to strings
print('Strings: ', ', '.join(str(e) for e in fib))