with open('text_5_4.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    new_lines = []
    for i in range(len(lines)):
        count = 0
        pattern_old = ['One', 'Two', 'Three', 'Four']
        pattern_new = ['Один', 'Два', 'Три', 'Четыре']
        while count < 4:
            if lines[i].count(pattern_old[count]) == 1:
                lines[i] = lines[i].replace(pattern_old[count], pattern_new[count])
                new_lines.append(lines[i])
            count += 1
    text_new = ''.join(new_lines)
    with open('text_5_4_1.txt', 'w', encoding='utf-8') as file2:
        file2.write(text_new)
