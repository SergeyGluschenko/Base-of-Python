import json

with open('text_5_7.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    total_list = []
    profit_dict = {}
    loss_dict = {}
    total_sum_profit = 0
    total_sum_loss = 0
    count_profit = 0
    count_loss = 0
    for line in lines:
        value = line.split(' ')
        profit = int(value[2]) - int(value[3])
        if profit > 0:
            total_sum_profit += profit
            count_profit += 1
            temp_profit_dict = {value[0]: profit}
            profit_dict.update(temp_profit_dict)
        else:
            total_sum_loss += profit
            count_loss += 1
            temp_loss_dict = {value[0]: profit}
            loss_dict.update(temp_loss_dict)
    average_profit = total_sum_profit / count_profit
    average_profit_dict = {'average_profit': average_profit}
    total_list.append(profit_dict)
    total_list.append(average_profit_dict)
    total_list.append(loss_dict)
    print(total_list)
    with open('text_5_7.json', 'w', encoding='utf-8') as file_json:
        json.dump(total_list, file_json, ensure_ascii=False)
