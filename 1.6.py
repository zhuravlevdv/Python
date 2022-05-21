while True:
    a = float(input("Сколько километров Вы пробежали в первый день? "))
    b = float(input("Ваша цель в км: "))
    if a <= 0 or b <= 0:
        print("Первый результат и цель должны быть больше нуля!")
    else:
        break
n = 1
if a >= b:
    print("Ты уже достиг цели, лентяй!")
else:
    while True:
        n = n + 1
        a += a * 0.1
        if a >= b:
            print(f"Вам потребуется {n} дней, чтобы достичь цели. Я в тебя верю!")
            break
        else:
            continue
