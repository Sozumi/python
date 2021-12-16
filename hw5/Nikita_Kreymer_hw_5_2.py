n = int(input('Введите число: '))
odd_to_n = (num for num in range(1, n+1, 2))

print(next(odd_to_n))
print(next(odd_to_n))
print(list(odd_to_n))
print(odd_to_n)
