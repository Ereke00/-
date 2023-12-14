# Чтение меток из файла
with open('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt', 'r', encoding='utf-8') as file:
    labels = file.read().split('-------------------------')

# Чтение текста сообщений из файла
with open('text.txt', 'r', encoding='utf-8') as file:
    messages = file.read().split('-------------------------')

# Извлечение текста из сообщений
texts = [message.split('\n')[3].strip() for message in messages]

# Сопоставление текстов с метками
labeled_messages = list(zip(labels, texts))

# Отображение первых нескольких меток и текстов для проверки
for label, text in labeled_messages[:5]:
    print("Метка:", label.strip())
    print("Текст сообщения:", text.strip())
    print("-------------------------")
