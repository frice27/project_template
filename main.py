from app.io.input import input_text_from_console, read_from_file_builtin, read_from_file_pandas
from app.io.output import output_text_to_console, write_text_to_file


def main():
    """Головна функція програми."""

    # 1. Отримати текст із консолі
    console_text = input_text_from_console()

    # 2. Зчитати текст із файлу за допомогою built-in
    file_text = read_from_file_builtin('data/sample.txt')  # приклад файлу

    # 3. Зчитати дані з файлу через pandas
    try:
        pandas_data = read_from_file_pandas('data/sample.csv')  # приклад csv файлу
    except FileNotFoundError:
        pandas_data = "Файл не знайдено."

    # Вивести результати в консоль
    output_text_to_console(console_text)
    output_text_to_console(file_text)
    output_text_to_console(pandas_data)

    # Записати результат у файл
    write_text_to_file('data/output.txt', f"{console_text}\n\n{file_text}\n\n{str(pandas_data)}")


if __name__ == "__main__":
    main()
