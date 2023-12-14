from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords

# Загружаем стоп-слова для русского языка из NLTK
nltk.download('stopwords')
stop_words = stopwords.words('russian')

# Считываем сообщения из файла
file_path = 'ОЧИЩЕННЫЕ_СООБЩЕНИЯ.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    messages = file.read().split('-------------------------\n')

# Выделяем тексты сообщений и их категории
texts = [message.split('\n') for message in messages]

# Очищаем тексты сообщений от лишних символов
cleaned_texts = []
for text in texts:
    cleaned_text = ' '.join(filter(lambda x: x != '' and 'спам:' not in x.lower() and 'категория:' not in x.lower(), text))
    cleaned_texts.append(cleaned_text)

# Создаем объект TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=1000, stop_words=stop_words)

# Преобразуем тексты в числовой формат с помощью TF-IDF
tfidf_features = tfidf_vectorizer.fit_transform(cleaned_texts)

# Получаем словарь слов и их индексов
feature_names = tfidf_vectorizer.get_feature_names_out()

# Получаем индексы слов с наибольшими TF-IDF значениями
top_indices = tfidf_features.toarray().argsort()[:, ::-1][:, :10]

# Получаем топ-10 слов для каждого текста
top_words = [[feature_names[idx] for idx in indices] for indices in top_indices]

