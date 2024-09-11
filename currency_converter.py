import requests

data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


# Получает текущую котировку
def exchange_rate_for_rub(currency):
    return data['Valute'][currency]['Value']


# Получает номинал обмена для валюты
def nominal(currency):
    return data['Valute'][currency]['Nominal']


# Конвертирует базовую валюту в валюту котировки
def convert(base_currency, quote_currency, summ):
    ex_rate_of_base_c = exchange_rate_for_rub(base_currency) if base_currency != "RUB" else 1
    ex_rate_of_quote_c = exchange_rate_for_rub(quote_currency) if quote_currency != "RUB" else 1

    nom_of_base_c = nominal(base_currency) if base_currency != "RUB" else 1
    nom_of_quote_c = nominal(quote_currency) if quote_currency != "RUB" else 1

    exchange_rate = round(ex_rate_of_base_c / ex_rate_of_quote_c *
                          nom_of_quote_c / nom_of_base_c, 4) if quote_currency != "RUB" else ex_rate_of_base_c
    converted_amount = round(summ * exchange_rate * nom_of_quote_c / nom_of_base_c, 4) if summ != 1 else None

    print(f"Курс {base_currency} к {quote_currency}: {exchange_rate}")
    if converted_amount is not None:
        print(f"{summ} {base_currency} в {quote_currency}: {converted_amount}")
