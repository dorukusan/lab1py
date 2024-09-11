import calendar

print("МЕНЮ\n\n[1] Знак числа\n[2] Високосный год\n"
      "[3] Гласная или согласная?\n[4] Калькулятор\n"
      "[5] Четное или нечетное?\n[6] Наибольшее число\n"
      "[7] Число в диапазоне?\n[8] Палиндром?\n[0] ВЫХОД")

while True:
    menu = int(input("\nВыберите пункт меню: "))
    if menu == 1:
        a = int(input("\nВведите число: "))
        if a > 0:
            print(a, "- положительное число")
        elif a < 0:
            print(a, "- отрицательное число")
        else:
            print(a, "- равно нулю")
    elif menu == 2:
        year = int(input('\nВведите год: '))

        if calendar.isleap(year):
            print(year, "- високосный год")
        else:
            print(year, "- не високосный год")
    elif menu == 3:
        letter = input("\nВведите букву: ")[0]
        if letter in "аеёиоуыэюяaeiouy":
            print(letter, "- гласная")
        else:
            print(letter, "- согласная")
    elif menu == 4:
        a = int(input("\nВведите первое число: "))
        b = int(input("Введите второе число: "))
        operation = "0"
        while operation not in "+-*/":
            operation = input("Введите операцию: ")[0]
        if operation == "+":
            print(a, operation, b, "=", a + b)
        elif operation == "-":
            print(a, operation, b, "=", a - b)
        elif operation == "*":
            print(a, operation, b, "=", a * b)
        else:
            print(a, operation, b, "", a / b)
    elif menu == 5:
        a = int(input("\nВведите число: "))
        if a % 2 == 0:
            print(a, "- четное")
        else:
            print(a, "- нечетное")
    elif menu == 6:
        a = int(input("\nВведите первое число: "))
        b = int(input("Введите второе число: "))
        c = int(input("Введите третье число: "))
        if a > b:
            biggest = a
        else:
            biggest = b
        if biggest < c:
            biggest = c
        print("Наибольшее число:", biggest)
    elif menu == 7:
        a, b = map(int, input("\nВведите диапазон через пробел: ").split())
        c = int(input("Введите число: "))
        if ((c >= a) and (c <= b)) or ((c <= a) and (c >= b)):
            print(f"Число {c} находится в заданном диапазоне от {a} до {b}")
        else:
            print(f"Число {c} не находится в заданном диапазоне от {a} до {b}")
    elif menu == 8:
        a = input("\nВведите строку: ")
        a = a.lower()
        string = "".join(c for c in a if c.isalpha())
        if string == string[::-1]:
            print("Данная строка - палиндром")
        else:
            print("Данная строка - не палиндром")
    elif menu == 0:
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        break
    else:
        print("Выберите существующий пункт!")
