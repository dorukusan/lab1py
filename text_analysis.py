import re


def count_words(text):
    text = re.sub(r'[^\w\s]', '', text.lower())
    print("Количество слов в тексте:", len([word for word in text.split() if word]))
