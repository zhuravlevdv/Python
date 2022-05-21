ingreds = []
features = {'name': '', 'quantity': '', 'units': ''}
analytics = {'name': [], 'quantity': [], 'units': []}
num = 0
while True:
    if input("To exit type Q, to continue press Enter: ").upper() == "Q":
        break
    num += 1
    f_copy = features.copy()
    for f in features:
        a = input(f"Enter {f}: ")
        f_copy[f] = int(a) if f in 'quantity' and a.isdigit() else a
        analytics[f].append(f_copy[f])
    ingreds.append((num, f_copy))
    print(f"\nIngredients\n{ingreds}")
    print(f"\nAnalytics:\n{'*' * 30}")
    for key, value in analytics.items():
        print(f"{key:>30}: {value}")
    print("*" * 30)

