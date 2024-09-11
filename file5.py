def print_hello():
    print("Привет, мир!")


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def count_vowels(word):
    count = 0
    for i in range(len(word)):
        if word[i] in "аеёиоуыэюяaeiouy":
            count += 1
    return count


def reverse_string(s):
    return s[::-1]


def check_palindrome(word):
    word = word.lower()
    string = "".join(c for c in word if c.isalpha())
    if string == string[::-1]:
        return True
    return False


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime(n):
    count = 0
    prime_num = 1
    while count < n:
        prime_num += 1
        if is_prime(prime_num):
            count += 1
    return prime_num


def fib(n):
    if n == 1:
        return 0
    if n in (2, 3):
        return 1
    return fib(n - 1) + fib(n - 2)


def circumstances(l):
    lst = []
    for i in range(1, round(l/2)+1):
        lst.append(prime(i))
        lst.append(fib(i))
    if l % 2 == 1:
        lst.pop()
    return lst


print("МЕНЮ\n\n[1] Привет, мир!\n[2] Четное или нечетное?\n"
      "[3] Количество гласных букв в строке\n[4] Перевернутая строка\n"
      "[5] Палиндром?\n[6] Простые числа\n[7] Числа Фибоначчи\n"
      "[8] Чередование простых и Фибоначчи\n[0] ВЫХОД")

while True:
    menu = int(input("\nВыберите пункт меню: "))
    if menu == 1:
        print_hello()
    elif menu == 2:
        num = int(input('\nВведите число: '))
        if is_even(num):
            print(f"{num} - четное число")
        else:
            print(f"{num} - нечетное число")
    elif menu == 3:
        word = input("\nВведите строку: ")
        print(f"Количество гласных: {count_vowels(word)}")
    elif menu == 4:
        s = input("\nВведите строку: ")
        print(f"Перевернутая строка: {reverse_string(s)}")
    elif menu == 5:
        word = input("\nВведите строку: ")
        if check_palindrome(word):
            print("Данная строка - палиндром")
        else:
            print("Данная строка - не палиндром")
    elif menu == 6:
        n = int(input("\nВведите число: "))
        print(f"{n}-ое простое число: {prime(n)}")
    elif menu == 7:
        n = int(input("\nВведите число: "))
        print(f"{n}-ое число Фибоначчи: {fib(n)}")
    elif menu == 8:
        n = int(input("\nВведите число: "))
        print(f"Список длины {n} с чередованием простых чисел и чисел Фибоначчи:\n {circumstances(n)}")
    elif menu == 0:
        print("\nВЫХОД ИЗ ПРОГРАММЫ")
        break
    else:
        print("Выберите существующий пункт!")
