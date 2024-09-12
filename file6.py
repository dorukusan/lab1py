import my_module as mm
import string_utils as su
import date_utils as du
import currency_converter as cc
import text_analysis as ta
import product_catalog as pc

print("МЕНЮ\n\n[1] Сумма двух чисел\n[2] Перевернутая строка\n"
      "[3] Високосный год\n[4] Конвертер валют\n"
      "[5] Количество слов в тексте\n[6] Каталог товаров\n[0] ВЫХОД")

while True:
    menu = int(input("\nВыберите пункт меню: "))
    if menu == 1:
        a = int(input("\nВведите первое число: "))
        b = int(input("Введите второе число: "))
        mm.add_numbers(a, b)
    elif menu == 2:
        s = input("\nВведите строку: ")
        su.reverse_string(s)
    elif menu == 3:
        year = int(input('\nВведите год: '))
        du.is_leap_year(year)
    elif menu == 4:
        base_currency = input("\nВведите базовую валюту: ")
        base_currency = base_currency.upper()
        summ = -1
        while summ <= 0:
            summ = float(input("Введите сумму базовой валюты: "))
        quote_currency = input("Введите валюту котировки: ")
        quote_currency = quote_currency.upper()
        cc.convert(base_currency, quote_currency, summ)
    elif menu == 5:
        text = input("\nВведите текст: ")
        ta.count_words(text)
    elif menu == 6:
        print("\nКАТАЛОГ\n\n[1] Добавить товар\n[2] Поиск по каталогу\n"
              "[3] Вывод каталога\n[0] ВЫХОД\n")

        while True:
            menu_prod = int(input("\nВыберите действие: "))
            if menu_prod == 1:
                name = input("\nВведите название товара: ")
                price = float(input("Введите стоимость товара: "))
                pc.add_product(name, price)
            elif menu_prod == 2:
                name = input("\nВведите название товара: ")
                pc.search_product(name)
            elif menu_prod == 3:
                pc.list_all_products()
            elif menu_prod == 0:
                print("\nВЫХОД ИЗ КАТАЛОГА")
                break
            else:
                print("Выберите существующий пункт!")

    elif menu == 0:
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        break
    else:
        print("Выберите существующий пункт!")
