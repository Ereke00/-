# Чтение данных из файла
with open('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

# Разделение на письма
emails = contents.split('-------------------------\n')
emails = [email.strip() for email in emails if email.strip()]

def extract_spam_category(email):
    spam_index = email.find("Метка спама:")  # Индекс строки с меткой спама
    category_index = email.find("Категория:")  # Индекс строки с категорией

    spam_label = email[spam_index + 12:].strip() if spam_index != -1 else None
    category_label = email[category_index + 11:].strip() if category_index != -1 else None

    return spam_label, category_label

def extract_email_text(email):
    start_index = email.find("Письмо")
    return email[start_index:].strip() if start_index != -1 else None

# Извлечение данных из каждого письма
for email in emails222:
    spam, category = extract_spam_category(email)
    email_text = extract_email_text(email)

    print("Текст письма:", email_text)
    print("Метка спама:", spam)
    print("Категория:", category)
    print("---------------------")

