def input_text_from_console():
    """Функція для вводу тексту з консолі.

    Повертає:
        str: Введений текст.
    """
    text = input("Введіть текст: ")
    return text


def read_from_file_builtin(filename):
    """Функція для зчитування тексту з файлу через вбудовані можливості Python.

    Аргументи:
        filename (str): Назва файлу для зчитування.

    Повертає:
        str: Вміст файлу.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def read_from_file_pandas(filename):
    """Функція для зчитування даних з файлу за допомогою бібліотеки pandas.

    Аргументи:
        filename (str): Назва файлу для зчитування.

    Повертає:
        DataFrame: Дані у вигляді таблиці.
    """
    import pandas as pd
    data = pd.read_csv(filename)
    return data
