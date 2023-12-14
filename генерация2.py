import random

# Словарь фраз для категории "проекты"
projects_phrases = [
    "Мы занимаемся разработкой веб-приложения для нашего клиента.",
    "Наша команда работает над проектом по машинному обучению.",
    "Мы создаем сайт для нового бизнеса с нуля.",
    "Разрабатываем новый алгоритм шифрования для безопасности данных.",
    # Другие фразы...
]

# Функция для генерации случайного текста проекта
def generate_project_text():
    # Выбор нескольких случайных фраз из списка
    selected_phrases = random.sample(projects_phrases, k=random.randint(2, 4))

    # Объединение выбранных фраз в текст проекта
    project_text = " ".join(selected_phrases)

    return project_text

# Пример использования функции для генерации текста проекта
random_project_text = generate_project_text()
print(random_project_text)

