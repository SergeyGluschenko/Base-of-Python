def int_func(text):
    print(text.title())


while True:
    user_text = input("Введите слово маленькими буквами или 'Q' для "
                      "завершения программы: ")
    if user_text == 'Q':
        break
    int_func(user_text)