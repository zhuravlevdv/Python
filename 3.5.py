mega_list = []
print(f"Enter any numbers divided by spaces as many times as you want. You will see the sum.\nType 'q' if your want to finish")
while True:
    iter_list = []
    nums = input("Your numbers:").split()
    for el in nums:
        try:
            el = float(el)
            iter_list.append(el)
            mega_list.append(el)
        except ValueError as err:
            if el == "q":
                break
            print(err)
            print('Try again')
    print(f"Sum of your last numbers is {sum(iter_list)}")
    print(f"Sum of all your number is {sum(mega_list)}")
    if "q" in nums:
        break
