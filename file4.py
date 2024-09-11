from random import randint

print("МЕНЮ\n\n[1] Список от 1 до 5\n[2] 5 слов в список\n"
      "[3] Сумма всех чисел в списке\n[4] Поиск числа в списке\n"
      "[5] Вывод наибольшего числа в списке\n"
      "[6] Удаление повторяющихся значений из списка\n"
      "[7] Ввод элементов в список\n[0] ВЫХОД")

while True:
    menu = int(input("\nВыберите пункт меню: "))
    if menu == 1:
        lst = []
        for i in range(1, 5+1):
            lst.append(i)
        print("\nСписок элементов от 1 до 5:", *lst)
    elif menu == 2:
        lst = []
        print("\nВведите 5 слов через Enter:")
        for i in range(5):
            lst.append(input())
        print(*lst)
    elif menu == 3:
        lst = [randint(-10, 10) for i in range(5)]
        print("Список:", *lst)
        result = 0
        for i in range(0, len(lst)):
            result += lst[i]
        print(f"Сумма всех чисел в списке {result}")
    elif menu == 4:
        lst = [randint(-5, 5) for i in range(5)]
        n = int(input("\nВведите число: "))
        print(f"Список: {lst}")
        if n in lst:
            print("Число найдено!")
        else:
            print("Число не найдено!")
    elif menu == 5:
        lst = [randint(-5, 5) for i in range(5)]
        print("Список:", *lst)
        lst.sort()
        print(f"Наибольшее число списка: {lst.pop()}")
    elif menu == 6:
        lst = [randint(1, 5) for i in range(10)]
        print("Исходный список:", *lst)
        new_lst = []
        for i in lst:
            if i not in new_lst:
                new_lst.append(i)
        print("Отредактированный список:", *new_lst)
    elif menu == 7:
        lst = []
        print("\nВведите слова через Enter. Введите 'стоп', чтобы закончить ввод:")
        word = ""
        while word.lower() != "стоп" or word.lower() != "stop":
            word = input()
            lst.append(word)
        lst.pop()
        print("Введенный список:", *lst)
    elif menu == 0:
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        break
    else:
        print("Выберите существующий пункт!")
