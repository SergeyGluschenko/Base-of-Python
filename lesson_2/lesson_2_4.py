user_text = input('Введите текст. Слова разделите побелом: ')
item = 1 # индекс для нумерации
for i in user_text.split():
    print(f' {item}. {i[:10]}')
    item += 1