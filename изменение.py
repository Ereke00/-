with open('ОЧИЩЕННЫЕ_СООБЩЕНИЯ.txt', 'r', encoding='utf-8') as file:
    contents = file.read()

# Удаление пустых строк
contents = "\n".join([line for line in contents.splitlines() if line.strip()])

# Добавление явных меток перед текстом письма
contents = contents.replace('спам:', 'Метка спама:')
contents = contents.replace('категория:', 'Категория:')
contents = contents.replace('Письмо', 'Текст письма:')

# Сохранение обновленной структуры в файл
with open('ИЗМЕНЕННЫЕ_СООБЩЕНИЯ1.txt', 'w', encoding='utf-8') as file:
    file.write(contents)
