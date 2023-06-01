from itertools import chain

# Using chain method, concatenating even and odd numbers
result = chain(range(0, 21, 2), range(1, 20, 2))
# showing the result
for number in result:
    print(number, end=" ")

print()
