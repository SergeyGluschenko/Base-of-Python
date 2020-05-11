user_second = int(input("Введите количество секунд: "))
hours = user_second // 3600
minute = (user_second - hours * 3600) // 60
second = (user_second - hours * 3600) % 60
# or second = (user_second - hours * 3600 - minute * 60)
print(f'{hours:02}:{minute:02}:{second:02}')