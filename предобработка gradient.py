from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')

# Функция для чтения данных из файла и извлечения текстов и категорий
def read_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    messages = data.split('-------------------------\n')
    return messages

# Функция для очистки текста
def preprocess_text(text):
    stop_words = set(stopwords.words('russian'))  # Загрузка русских стоп-слов
    lemmatizer = WordNetLemmatizer()  # Порядок лемматизации слов
    tokens = word_tokenize(text)
    processed_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stop_words]
    processed_text = ' '.join(processed_tokens)
    return processed_text

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
print(len(texts))
print(len(categories))

# Преобразование текстов в числовые векторы с помощью TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(categories)
# Обучение модели Gradient Boosting
gb = GradientBoostingClassifier(random_state=42)
gb.fit(X, y)

# Функция для получения ключевых слов для категории "Проекты"
def get_keywords_for_category(category_name, vectorizer, model):
    category_indices = [i for i, category in enumerate(categories) if category == category_name]
    category_X = X[category_indices]
    category_keywords = {}
    feature_names = vectorizer.get_feature_names_out()
    sorted_indices = np.argsort(model.feature_importances_)[::-1]
    top_keywords = [feature_names[ind] for ind in sorted_indices[:10]]  # Получить топ 10 ключевых слов
    category_keywords[category_name] = top_keywords
    return category_keywords

# Получение ключевых слов для категории "Проекты"
projects_keywords = get_keywords_for_category("Проекты", vectorizer, gb)
print("Ключевые слова для категории 'Проекты':")
print(projects_keywords)






# Функция для классификации пользовательского сообщения
def classify_message(message):
    message_vectorized = vectorizer.transform([message])
    prediction = gb.predict(message_vectorized)
    return prediction[0]

# Пример использования:
for i in range(0, 10):
    user_message = input("Введите ваше сообщение: ")
    result = classify_message(user_message)
    print(f"Категория сообщения: {result}")
