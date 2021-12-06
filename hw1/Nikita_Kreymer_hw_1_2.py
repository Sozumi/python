a = []
for i in range(1, 1001):
    if i % 2 != 0:
        a.append(i ** 3)
print(a)


sum1 = 0
for num in a:
    summ1 = 0
    i = num
    while num != 0:
        summ1 += num % 10
        num = num // 10
    if summ1 % 7 == 0:
        sum1 += i
print(sum1)


sum2 = 0
for num in a:
    summ2 = 0
    i = num
    num += 17
    while num != 0:
        summ2 += num % 10
        num = num // 10
    if summ2 % 7 == 0:
        sum2 += i
print(sum2)