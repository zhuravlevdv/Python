def int_func(words=str):
    chars = "qwertyuiopasdfghjklzxcvbnm "
    if set(words).difference(chars):
        print("Error! Enter only latin characters in lowercase divided by spaces")
    else:
        print(words.title())


int_func(input("Enter any words in lowercase divided by spaces: "))
