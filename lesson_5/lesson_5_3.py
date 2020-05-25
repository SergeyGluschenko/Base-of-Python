with open('text_5_3.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        temp = lines[i].split(' ')
        if float(temp[1]) < 20000:
            print(temp[0])
