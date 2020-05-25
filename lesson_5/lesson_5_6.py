with open('text_5_6.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    dict_lesson = {}
    for line in range(len(lines)):  # разбиваем текст на строки
        words = lines[line].split(' ')
        key_modif = words[0].replace(':', '')  # заменили если есть двоеточее
        total_lesson = 0
        for word in words:  # разбиваем строки на слова
            num_lesson = ''
            for symbol in word: # разбиваем слова на символы
                if symbol.isdigit() == True:
                    num_lesson += symbol
                else:
                    break
            if len(num_lesson) > 0:
                total_lesson += int(num_lesson)
        dict_temp_for = {key_modif: total_lesson}
        dict_lesson.update(dict_temp_for)

print(dict_lesson)
