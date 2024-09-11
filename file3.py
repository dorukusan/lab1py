print("МЕНЮ\n\n[1] Все от 1 до 10\n[2] Четные от 1 до 20\n"
      "[3] От 10 до 1 с шагом 2\n[4] От 1 до введенного числа\n"
      "[5] Таблица умножения для 5\n[6] Факториал\n[0] ВЫХОД")

while True:
    menu = int(input("\nВыберите пункт меню: "))
    if menu == 1:
        print("\nВсе числа от 1 до 10:")
        i = 1
        while i <= 10:
            print(i)
            i += 1
    elif menu == 2:
        print("\nЧетные числа от 20 до 1:")
        for i in range(1, 20+1):
            if i % 2 == 0 and i != 0:
                print(i)
    elif menu == 3:
        print("\nВсе числа от 1 до 10 с шагом 2:")
        for i in range(20, 1, -2):
            print(i)
    elif menu == 4:
        n = int(input("\nВведите число: "))
        print(f"Все числа от 1 до {n} :")
        i = 1
        while i <= n:
            print(i)
            i += 1
    elif menu == 5:
        print("\nТаблица умножения для 5:")
        n = 5
        for i in range(1, 10+1):
            print(f"{n} * {i} = {5 * i}")
    elif menu == 6:
        n = int(input("\nВведите число: "))
        print(f"Факториал числа {n} :")
        i = 1
        factorial = 1
        while i <= n:
            factorial *= i
            i += 1
        print(factorial)
    elif menu == 0:
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        break
    else:
        print("Выберите существующий пункт!")
