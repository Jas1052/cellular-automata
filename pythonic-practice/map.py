a = [1, 2, 3, 4, 5]
b = []

for val in a:
    b.append(val**2)
print(b)

a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x**2, a))
print(b)
