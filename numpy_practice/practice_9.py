# Блок І. Імпорти та створення тестових даних
import pandas as pd
import numpy as np

# Завдання 1: Імпортувати бібліотеки pandas та numpy

# Завдання 2: Створити тестовий датафрейм із даними про покупців
buyers = [
    ["Іван", "Петров", "2024-04-01", 5, True],
    ["Марія", "Іванова", "2024-03-15", 2, False],
    ["Олег", "Сидоренко", "2024-02-28", 8, True],
    ["Анна", "Ковальчук", None, 1, False],
    ["Дмитро", "Шевченко", "2024-01-10", 3, True]
]

columns = ["Ім'я", "Прізвище", "Дата останнього замовлення", "Кількість товарів", "Картка лояльності"]
customer_df = pd.DataFrame(buyers, columns=columns)
print(customer_df)

# Блок ІІ. Завантаження основного датафрейму

# Завдання 3: Завантажити CSV файл із даними атак
try:
    attacks_df = pd.read_csv("missile_attacks_daily.csv")
except FileNotFoundError:
    print("Помилка: файл missile_attacks_daily.csv не знайдено. Перевірте шлях!")
    exit()

# Блок ІІІ. Аналіз структури даних

# Завдання 4: Вивести перші 20 рядків
print(attacks_df.head(20))

# Завдання 5: Вивести форму датафрейму
print("Розміри датафрейму:", attacks_df.shape)

# Завдання 6: Інформація про кожну колонку
print(attacks_df.info())

# Альтернативний формат виводу інформації про колонки
summary = pd.DataFrame({
    "Назва": attacks_df.columns,
    "Тип даних": attacks_df.dtypes.values,
    "Непустих": attacks_df.count().values
})
print(summary)

# Завдання 7: Статистичний опис числових колонок
print(attacks_df.describe())

# Завдання 8: Порахувати кількість унікальних значень у кожній колонці
print(attacks_df.nunique())

# Завдання 9: Колонка з найменшою кількістю унікальних значень
min_unique_col = attacks_df.nunique().idxmin()
print(f"Найменше унікальних значень у колонці: {min_unique_col}")
print(attacks_df[min_unique_col].value_counts())

# Блок IV. Очищення даних

# Завдання 11: Привести launched до типу Int64
attacks_df['launched'] = attacks_df['launched'].astype('Int64')
print(attacks_df['launched'].head())

# Завдання 12: Видалити колонки, де менше 30% даних
threshold_count = attacks_df.shape[0] * 0.3
attacks_df = attacks_df.loc[:, attacks_df.count() >= threshold_count]
print("Залишені колонки:", list(attacks_df.columns))

# Завдання 13: Прибрати дублікати та некоректні значення тривалості
start_count = len(attacks_df)
attacks_df = attacks_df.drop_duplicates()
attacks_df['time_start'] = pd.to_datetime(attacks_df['time_start'], errors='coerce')
attacks_df['time_end'] = pd.to_datetime(attacks_df['time_end'], errors='coerce')
attacks_df = attacks_df[attacks_df['time_end'] > attacks_df['time_start']]
attacks_df.reset_index(drop=True, inplace=True)
end_count = len(attacks_df)
print(f"Видалено {start_count - end_count} записів.")

# Завдання 14: Вивести всі рядки з пропущеними даними
print(attacks_df[attacks_df.isnull().any(axis=1)])

# Блок V. Обробка даних

# Завдання 15: Розрахувати середній відсоток збиття
successful_hits = attacks_df[['launched', 'destroyed']].dropna()
successful_hits['hit_ratio'] = (successful_hits['destroyed'] / successful_hits['launched']) * 100
avg_hit_percent = successful_hits['hit_ratio'].mean()
print(f"Середній відсоток збиття: {avg_hit_percent:.2f}%")

# Завдання 16: Топ-7 моделей за кількістю запусків
import json

models_df = attacks_df[['model', 'launched']].dropna()
model_launch_sum = models_df.groupby('model')['launched'].sum()
top_models = model_launch_sum.sort_values(ascending=False).head(7)
top_models_dict = top_models.to_dict()

with open("top_7_models.json", "w", encoding="utf-8") as f:
    json.dump(top_models_dict, f, ensure_ascii=False, indent=4)

print(json.dumps(top_models_dict, ensure_ascii=False, indent=4))

# Завдання 17: День із найбільшою кількістю влучань
attacks_df['missed'] = attacks_df['launched'].fillna(0) - attacks_df['destroyed'].fillna(0)
worst_day = attacks_df.loc[attacks_df['missed'].idxmax()]
print("Найгірший день атаки:", worst_day['time_start'])
print("Кількість влучань:", worst_day['missed'])

# Завдання 18: Найдовші та найкоротші атаки по місяцях
attacks_df['attack_duration'] = attacks_df['time_end'] - attacks_df['time_start']
attacks_df['year'] = attacks_df['time_start'].dt.year
attacks_df['month'] = attacks_df['time_start'].dt.month
valid_attacks = attacks_df.dropna(subset=['attack_duration', 'year', 'month'])

shortest = valid_attacks.loc[valid_attacks.groupby(['year', 'month'])['attack_duration'].idxmin()]
longest = valid_attacks.loc[valid_attacks.groupby(['year', 'month'])['attack_duration'].idxmax()]
result_df = pd.concat([shortest, longest]).sort_values(['year', 'month', 'attack_duration'])

result_df[['year', 'month', 'attack_duration']].to_csv("attack_durations_by_month.csv", index=False)
print(result_df[['year', 'month', 'attack_duration']])