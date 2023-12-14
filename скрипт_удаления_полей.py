import re

def remove_fields_from_email(email_text):
    # Регулярные выражения для определения полей
    fields_to_remove = ['Тема:', 'От:', 'Дата:', 'Кому:', 'Reply-to:']

    cleaned_email = []
    lines = email_text.split('\n')
    for line in lines:
        for field in fields_to_remove:
            if line.startswith(field):
                break
        else:
            cleaned_email.append(line)

    return '\n'.join(cleaned_email)

def process_dataset(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        dataset = file.read()

    # Разделение датасета на сообщения
    emails = re.split(r'(спам: \d+|категория: \w+)', dataset)[1:]

    cleaned_emails = []
    for i in range(0, len(emails), 2):
        email = emails[i] + emails[i+1]
        cleaned_email = remove_fields_from_email(email)
        cleaned_emails.append(cleaned_email)

    # Запись очищенных данных в новый файл
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n\n'.join(cleaned_emails))

# Укажите путь к вашему файлу ввода и файлу вывода
input_file_path = 'ВСЕ_СООБЩЕНИЯ.txt'
output_file_path = 'ОЧИЩЕННЫЕ_СООБЩЕНИЯ.txt'

process_dataset(input_file_path, output_file_path)
