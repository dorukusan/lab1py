all_prod = {}


def add_product(name, price):
    all_prod.update({name: price})


def search_product(name):
    prod = all_prod.get(name)
    if prod is None:
        print("Товар отсутствует!")
    else:
        print(f"Товар найден! Стоимость товара: {prod}")


def list_all_products():
    print("Товар / Стоимость")
    for name, price in all_prod.items():
        print(f"{name}: {price}")