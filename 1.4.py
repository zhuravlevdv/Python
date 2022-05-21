n = int(input("Vvedite chislo: "))
while n < 0:
    n = int(input("Нет, введите целое положительное число: "))
max_d = 0
while n > 0:
    d = n % 10
    if d > max_d:
        max_d = d
        if max_d == 9:
            break
    n = n // 10
print(max_d)

#---------------------odnoy strochkoy----------------------------

print(max(input()))

