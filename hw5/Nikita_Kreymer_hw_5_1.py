def odd_number(n):
    for num in range(1, n+1, 2):
        yield num


odd_to_n = odd_number(13)

print(next(odd_to_n))
print(next(odd_to_n))
print(list(odd_to_n))
print(odd_to_n)
