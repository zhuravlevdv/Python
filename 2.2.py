mega_list = input("Please, enter random numbers or letters: ")
if mega_list.count(' ') > 0:
    mega_list = list(mega_list.split())
else:
    mega_list = list(mega_list)
print(f"mega_list = {mega_list}")
for i in range(1, len(mega_list), 2):
    mega_list[i - 1], mega_list[i] = mega_list[i], mega_list[i - 1]
reversed_list = mega_list
print(reversed_list)

#----------------------var_2----------------------------------------

new_list = input("Please, enter random numbers or letters: ")
if new_list.count(' ') > 0:
    new_list = list(new_list.split())
else:
    new_list = list(new_list)
print(f"new_list = {new_list}")
for i in range(1, len(new_list), 2):
    new_list.insert(i - 1, new_list.pop(i))
new_reversed_list = new_list
print(new_reversed_list)
