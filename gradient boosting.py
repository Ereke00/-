from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

# Функция для чтения данных из файла и извлечения текстов и категорий
def read_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    messages = data.split('-------------------------\n')
    return messages

# Чтение данных из файлов
file1_messages = read_messages('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt')
file2_messages = read_messages('text.txt')

# Создание списка текстов и соответствующих категорий
texts = []
categories = []

# Извлечение текстов и категорий из сообщений
for message in file1_messages + file2_messages:
    lines = message.split('\n')
    for line in lines:
        if line.startswith('Категория'):
            category = line.split(': ')[1]
            categories.append(category)
            text = '\n'.join(lines[3:-5])  # Извлечение текста сообщения
            texts.append(text)

# Преобразование текстов в числовые векторы с помощью TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(categories)

# Обучение модели Gradient Boosting
gb = GradientBoostingClassifier(random_state=42)
gb.fit(X, y)

# Функция для классификации пользовательского сообщения
def classify_message(message):
    message_vectorized = vectorizer.transform([message])
    prediction = gb.predict(message_vectorized)
    return prediction[0]

for i in range(0,5):
    # Пример использования:
    user_message = input("Введите ваше сообщение: ")
    result = classify_message(user_message)
    print(f"Категория сообщения: {result}")

