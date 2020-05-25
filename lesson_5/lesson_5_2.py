with open('text_5_2.txt', 'r') as file:
    lines = file.readlines()
    print(f'Всего в документе {len(lines)} строк')
    for i in range(len(lines)):
        quantity_word = len(lines[i].split(" "))
        if lines[i] == '\n':  # если нет слов и есть только перенос строки
            quantity_word = 0
        print(f'{i+1}-я строка содержет слов ->{quantity_word}')