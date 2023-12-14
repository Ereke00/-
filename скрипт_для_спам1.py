# Список файлов для объединения
files_to_merge = ['новый_Вакансии.txt', 'новый_ПРОЕКТЫ.txt', 'Общ_Spam.txt','Общ_спам3.txt']

# Открываем файл для записи всех сообщений
with open('ВСЕ_СООБЩЕНИЯ.txt', 'w', encoding='utf-8') as output_file:
    # Проходимся по каждому файлу для объединения
    for file_name in files_to_merge:
        # Открываем файл с сообщениями для чтения
        with open(file_name, 'r', encoding='utf-8') as file:
            # Читаем содержимое файла
            messages = file.read()
            # Записываем содержимое в общий файл
            output_file.write(messages)
