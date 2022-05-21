x = float(input("Enter any positive number: "))
while x <= 0:
    print("Error. Try again.")
    x = float(input("Enter any positive number: "))

y = int(input("Enter any negative integer: "))
while y >= 0:
    print("Error. Try again.")
    y = int(input("Enter any negative integer: "))


def my_func(x, y):
    p = x ** y
    return p


def my_func_2(x, y):
    num = 1
    p_2 = 1 / x
    while num < abs(y):
        num += 1
        p_2 = p_2 / x
    return p_2


print(my_func(x, y))
print(my_func_2(x, y))
