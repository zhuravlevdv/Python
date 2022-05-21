rating = [9, 7, 7, 5, 3, 2, 2]
a = int(input("Enter a number: "))
while a < 1:
    print("No! A number should be greater than zero.")
    a = int(input("Try again: "))
rating.append(a)
rating.sort()
rating.reverse()
print(rating)

#--------------------------var_2----------------------------

my_list = [7, 5, 5, 5, 4, 3]
b = int(input("Enter a number: "))
while b < 1:
    print("No! A number should be greater than zero.")
    b = int(input("Try again: "))
if b in my_list[:-1]:
    for el in my_list:
        if b > el:
            i = my_list.index(el)
            my_list.insert(i, b)
            break
elif b <= min(my_list):
    my_list.append(b)
elif b > max(my_list):
    my_list.insert(0, b)
print(my_list)
