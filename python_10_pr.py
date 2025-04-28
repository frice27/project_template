# Завдання 1: Імпорт необхідних бібліотек
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завдання 2: Зчитування даних
file_path = "train.csv"
titanic = pd.read_csv(file_path)

# Виведення базової інформації про набір даних
print("Інформація про набір даних Titanic:")
print(titanic.info())

# Завдання 3: Графік виживання пасажирів (діаграма кругова)
survived_counts = titanic['Survived'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(
    survived_counts,
    labels=['Загинули', 'Вижили'],
    autopct='%1.1f%%',
    startangle=140,
    colors=['#fa8072', '#87cefa']
)
plt.title('Відсоткове співвідношення виживших і загиблих')
plt.axis('equal')
plt.show()

# Завдання 4: Стовпчиковий графік виживання за статтю
survival_by_sex = titanic.groupby(['Sex', 'Survived']).size().reset_index(name='Count')
sns.barplot(data=survival_by_sex, x='Sex', y='Count', hue='Survived', palette='Set2')
plt.title('Виживання пасажирів за статтю')
plt.xlabel('Стать')
plt.ylabel('Кількість пасажирів')
plt.tight_layout()
plt.show()

# Завдання 5: Візуалізація пропущених значень
missing_data = titanic.isnull().sum()
missing_data = missing_data[missing_data > 0]

plt.figure(figsize=(10, 6))
missing_data.sort_values(ascending=True).plot(kind='barh', color='lightcoral')
plt.title('Кількість пропущених значень у кожній колонці')
plt.xlabel('Кількість пропусків')
plt.tight_layout()
plt.show()

# Завдання 6: Розподіл віку пасажирів за класами і виживанням
plt.figure(figsize=(12, 6))
sns.violinplot(x='Pclass', y='Age', hue='Survived', data=titanic, split=True, palette='muted')
plt.title('Розподіл віку за класами і виживанням')
plt.xlabel('Клас каюти')
plt.ylabel('Вік пасажира')
plt.legend(title='Вижив')
plt.tight_layout()
plt.show()

# Завдання 7: Гістограма розподілу віку
plt.figure(figsize=(10, 6))
sns.histplot(titanic['Age'].dropna(), bins=30, kde=True, color='skyblue')
plt.axvline(titanic['Age'].median(), color='red', linestyle='-', label='Медіана')
plt.axvline(titanic['Age'].mean(), color='green', linestyle='--', label='Середнє значення')
plt.title('Гістограма розподілу віку пасажирів')
plt.xlabel('Вік')
plt.ylabel('Кількість пасажирів')
plt.legend()
plt.tight_layout()
plt.show()

# Завдання 8: Рівень виживання за класами пасажирів
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=titanic, palette='pastel', errorbar=None)
plt.title('Рівень виживання залежно від класу')
plt.xlabel('Клас (1 = Верхній, 2 = Середній, 3 = Нижній)')
plt.ylabel('Ймовірність виживання')
plt.ylim(0, 1)
plt.tight_layout()
plt.show()
