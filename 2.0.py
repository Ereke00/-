from flask import Flask, jsonify, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np
from flask_cors import CORS
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)
CORS(app)

def read_messages(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    messages = data.split('-------------------------\n')
    return messages

def preprocess_text(text):
    stop_words = set(stopwords.words('russian'))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    processed_tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens if token.lower() not in stop_words]
    processed_text = ' '.join(processed_tokens)
    return processed_text

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

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)
y = np.array(categories)

gb = GradientBoostingClassifier(random_state=42)
gb.fit(X, y)

def classify_message(message):
    message_vectorized = vectorizer.transform([message])
    prediction = gb.predict(message_vectorized)
    return prediction[0]

@app.route('/predict_category', methods=['POST'])
def predict_category():
    data = request.get_json()
    message = data['message']
    print(message)
    prediction = classify_message(message)
    return jsonify({'category': prediction})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
    print("APPP IS TERR")
