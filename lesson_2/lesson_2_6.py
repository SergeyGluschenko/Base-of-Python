list_goods = []  # пустой список товаров
count_good = 1  # счетчик товарных позиций. Начинайм с единици
while True:
    list_keys = ['название', 'цена', 'количество', 'ед'] # список пунктов для заполнения
    dict_temp = {}  # временный словарь для хранения временных данных о товаре
    for i in list_keys:
        user_text = input(f'Введете {i} {count_good}-го товара: ')
        dict_temp_for = {i: user_text}
        dict_temp.update(dict_temp_for)
    list_one_good = (count_good, dict_temp)
    list_goods.append(list_one_good) # к общему описанию добавляем описание каждого товара
    count_good += 1 # увеличиваем нумирацию счетчика товаров
    split = input("Еще есть товор для ввода? (Y/N): ") # проверяем есть ли еще товары для ввода
    if split.upper() == 'N':
        break

print(list_goods)

analytics_goods = input("Хотите собрать аналитику на товары? (Y/N): ")
if analytics_goods.upper() == 'Y': # узнаем хочет ли user получить аналитику
    dict_analysis = {}
    while True:
        item = input("На что собрать аналитику?('название', 'цена', 'количество', 'ед'): ")
        val_list = []
        count = 0
        while count < len(list_goods): # из описания товаваров по ключу достаем значение
            val_list.append(list_goods[count][1][item])
            dict_analysis_for = {item: val_list}
            dict_analysis.update(dict_analysis_for)
            count += 1
        split = input("Еще нужна какая либо аналитика на товор? (Y/N): ")
        if split.upper() == 'N':
            break
print(dict_analysis)  # выводим аналитику на товары
