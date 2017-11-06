def subset(numbers):
    if numbers == []:
        return [[]]

    x = subset(numbers[1:])

    return x + [[numbers[0]] + y for y in x]

print(subset([1, 2, 3]))
