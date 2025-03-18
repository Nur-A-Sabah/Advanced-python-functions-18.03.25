numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = [i for i in numbers if i % 2 == 0]
odd = [i for i in numbers if i % 2 != 0]

print(even)
print(odd)

fruits = ["apple", "banana", "grape", "mango"]

capFruit = [fruit.capitalize() for fruit in fruits]
print(capFruit)


upperFruit = [fruit.upper() for fruit in fruits]
print(upperFruit)
