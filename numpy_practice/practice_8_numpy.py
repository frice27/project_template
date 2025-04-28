# I. NumPy
import numpy as np

# 2. (3б) Визначити список з оцінками студента(ки) за семестр. Створити одновимірний масив numpy.
grades = [95, 88, 76, 64, 85, 91, 70]
grades_array = np.array(grades)

# 3. (4б) Список зі списками цін у магазинах. Створити матрицю numpy.
prices = [
    [20.5, 35.0, 29.9, 80.0],
    [19.9, 36.5, 30.0, 78.5],
    [21.0, 34.5, 31.0, 82.0]
]
prices_array = np.array(prices)

# 4. (3б) Тип даних значень з масивів завдань 2 та 3.
print(grades_array.dtype)
print(prices_array.dtype)

# 5. (3б) Форми масивів завдань 2 та 3.
print(grades_array.shape)
print(prices_array.shape)

# 6. (5б) Пояснення + створення вектора-стовпця.
# Для масиву із завдання 2 ми отримали форму (7,), оскільки він є одновимірним масивом — лише один рядок без додаткових осей.
# Щоб створити вектор-стовпець, треба додати нову вісь.
grades_column = grades_array.reshape(-1, 1)

# 7. (6б) Різниця між Python списком та NumPy масивом.
# - Python список може містити елементи різних типів, тоді як NumPy масиви мають елементи одного типу (гомогенні).
# - Операції з NumPy масивами значно швидші та ефективніші для великих обчислень.
# - NumPy підтримує векторизовані операції, що дозволяє працювати з масивами без явних циклів.

# 8. (7б) Створити масив динаміки прибутку.
profit = np.linspace(0, 1000.5, 7)

# 9. (8б) Вертикальне та горизонтальне об’єднання масивів.
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vertical_stack = np.vstack((a, b))
horizontal_stack = np.hstack((a, b))

print("Vertical stack:\n", vertical_stack)
print("Horizontal stack:\n", horizontal_stack)

# 10. (12б) Функція для транспонування масиву через reshape.
def transpose_array(arr):
    """
    Функція для транспонування масиву через зміну його форми.
    """
    return arr.reshape(arr.shape[1], arr.shape[0])

# Приклад використання
array_example = np.array([[1, 2], [3, 4], [5, 6]])
print(transpose_array(array_example))

# 11. (7б) Операції з масивами.
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

# Поелементне додавання
add = x + y

# Поелементне віднімання
subtract = x - y

# Множення масиву на число
multiply_scalar = x * 3

# Поелементне множення
elementwise_multiply = x * y

# Матричне множення
matrix_multiply = np.dot(x, y)

print("Add:", add)
print("Subtract:", subtract)
print("Multiply by scalar:", multiply_scalar)
print("Elementwise multiply:", elementwise_multiply)
print("Matrix multiply:", matrix_multiply)

# 12. (7б) Робота з двовимірним масивом.
matrix = np.array([
    [3, 7, 1],
    [5, 2, 9],
    [8, 4, 6]
])

# Мінімальне число
print(matrix.min())

# Максимальне число
print(matrix.max())

# Сума чисел
print(matrix.sum())

# Мінімальні числа для кожного рядка
print(matrix.min(axis=1))

# Максимальні числа для кожного стовпчика
print(matrix.max(axis=0))

# 13. (6б) Вибрати перший та другий стовпчики без першого та останнього рядка.
print(matrix[1:-1, 0:2])

# 14. (7б) Унікальні значення та їх частоти.
matrix_with_duplicates = np.array([
    [1, 2, 2],
    [3, 1, 3],
    [1, 2, 3]
])

unique_elements, counts = np.unique(matrix_with_duplicates, return_counts=True)

print("Унікальні елементи:", unique_elements)
print("Їх кількість:", counts)


