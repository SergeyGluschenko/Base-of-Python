with open('text.txt', 'w') as file:
    while True:
        info = input("Enter some text: ")
        if info == '':
            break
        else:
            file.write(f'{info}\n')