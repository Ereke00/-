from sklearn.feature_extraction.text import TfidfVectorizer

# Чтение содержимого файла
with open('ОЧИЩЕННЫЕ_СООБЩЕНИЯ.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

# Разделение содержимого файла на письма
emails = contents.split('-------------------------\n')

# Удаление пустых писем, если они есть
emails = [email.strip() for email in emails if email.strip()]

# Инициализация векторизатора TF-IDF
tfidf_vectorizer = TfidfVectorizer(max_features=1000)

# Проход по каждому письму и TF-IDF векторизация
for email in emails:
    # Преобразование текстов в TF-IDF признаки для каждого письма
    X_tfidf = tfidf_vectorizer.fit_transform([email])
    
    # Получение списка всех слов
    words_tfidf = tfidf_vectorizer.get_feature_names_out()
    
    # Получение индексов слов с наибольшими значениями TF-IDF для каждого документа
    top_tfidf_words_indexes = X_tfidf.toarray().argsort(axis=1)[:, ::-1][:, :10]

    print("Top 10 слов по TF-IDF для каждого документа:")
    for i, indexes in enumerate(top_tfidf_words_indexes):
        words = [words_tfidf[idx] for idx in indexes]
        print(f"Документ {i + 1}: {', '.join(words)}")
