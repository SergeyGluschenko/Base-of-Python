user_revenue = int(input("Введите выручку вашей фирмы в рублях: "))
user_costs = int(input("Введите издержки вашей фирмы в рублях: "))
if user_revenue > user_costs:
    print("Ваша фирма работает с прибылью!")
    print('Рентабельность фирмы: ' + str((user_revenue - user_costs) / user_revenue))
    number_staff = int(input("Введите количество сотрудников на вашей фирме: "))
    print('Прибыль фирмы на одного сотрудника: ' + str((user_revenue - user_costs) / number_staff))
else:
    print(f"Ваша фирма работает с убытком!")



