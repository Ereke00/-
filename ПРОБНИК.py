from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

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

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, categories, test_size=0.2, random_state=42)

# Инициализация и обучение модели SVM с учетом взвешивания классов
svm = SVC(kernel='linear', class_weight='balanced')
svm.fit(X_train, y_train)


# Предсказание категорий для тестовых данных
predictions = svm.predict(X_test)

conf_matrix = confusion_matrix(y_test, predictions)


# Оценка точности модели
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Вывод отчета о классификации
print(classification_report(y_test, predictions))
# Код для интерфейса
user_input = input("Введите сообщение (для выхода наберите 'exit'): ")


    # Преобразование введенного текста в числовой вектор
user_input_vector = vectorizer.transform([user_input])

    # Предсказание категории для введенного текста
predicted_category = svm.predict(user_input_vector)[0]
print(f"Предсказанная категория: {predicted_category}")

