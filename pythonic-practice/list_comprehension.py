a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

output1 = [number**2 for number in a]
print(output1)
# [1, 4, 9, 16]

c = [first * second for first in a for second in b]
d = []
for first in a:
    for second in b:
        d.append(first*second)
        
print(c)
print(d)
# [1, 2, 3, 4, 2, 4, 6, 8, 3, 6, 9, 12, 4, 8, 12, 16]
