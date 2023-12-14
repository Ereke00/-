def extract_emails(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        emails = []
        current_email = ''
        for line in lines:
            line = line.strip()
            if line.startswith('-'):
                if current_email:
                    emails.append(current_email.strip())
                    current_email = ''
            elif line and not line.startswith('Метка спама') and not line.startswith('Категория'):
                current_email += line + '\n'
        if current_email:  # Добавляем последнее письмо, если оно есть
            emails.append(current_email.strip())
        return emails

def save_emails_to_file(emails, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for email in emails:
            file.write(email + '\n-------------------------\n')

# Считываем тексты писем из файла
emails = extract_emails('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt')

# Сохраняем тексты писем в другой файл
save_emails_to_file(emails, 'text.txt')
