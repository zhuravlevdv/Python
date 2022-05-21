def my_func(a, b, c):
    s = a + b + c - min(a, b, c)
    return s


print(my_func(float(input("Number 1: ")), float(input("Number 2: ")), float(input("Number 3: "))))
