def mega_f(a_1=float, a_2=float):
    try:
        dev = a_1 / a_2
        print("Devision: ")
        return dev
    except ZeroDivisionError as err:
        print("Error! Try again")
        return err


print(mega_f(float(input("Number 1: ")), float(input("Number 2: "))))

