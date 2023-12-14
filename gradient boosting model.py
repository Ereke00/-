from sklearn.ensemble import GradientBoostingClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Функция чтения сообщений из файла
def read_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    messages = data.split('-------------------------\n')
    return messages

# Функция предобработки текста
def preprocess_text(text):
    stop_words = set(stopwords.words('russian'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    processed_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stop_words]
    processed_text = ' '.join(processed_tokens)
    return processed_text

# Чтение сообщений
file1_messages = read_messages('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt')
file2_messages = read_messages('text.txt')

texts = []
categories = []

for message in file1_messages + file2_messages:
    lines = message.split('\n')
    for line in lines:
        if line.startswith('Категория'):
            category = line.split(': ')[1]
            categories.append(category)
            text = '\n'.join(lines[3:-5])
            preprocessed_text = preprocess_text(text)
            texts.append(preprocessed_text)

# Инициализация и обучение TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)  # Обучение и трансформация текстов

y = categories

# Обучение модели Gradient Boosting Classifier
gb = GradientBoostingClassifier(random_state=42)
gb.fit(X, y)

# Функция классификации сообщения
def classify_message_with_gb(message):
    processed_message = preprocess_text(message)
    message_vectorized = vectorizer.transform([processed_message])
    prediction = gb.predict(message_vectorized)
    return prediction[0]

# Предсказания для тренировочных данных
y_pred = gb.predict(X)

# Оценка точности модели
accuracy = accuracy_score(y, y_pred)
print("Accuracy:", accuracy)

# Построение матрицы ошибок
conf_matrix = confusion_matrix(y, y_pred)
print("Confusion Matrix:")
print(conf_matrix)

# Визуализация матрицы ошибок
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=gb.classes_, yticklabels=gb.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# Пример использования
sample_message = "Топ вакансии для вас. Успейте откликнуться на них"
gb_prediction = classify_message_with_gb(sample_message)
print("Predicted category using Gradient Boosting:", gb_prediction)
