def output_text_to_console(text):
    """Функція для виведення тексту в консоль.

    Аргументи:
        text (str): Текст для виводу.
    """
    print(text)


def write_text_to_file(filename, text):
    """Функція для запису тексту у файл через вбудовані можливості Python.

    Аргументи:
        filename (str): Назва файлу для запису.
        text (str): Текст, який потрібно записати.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
