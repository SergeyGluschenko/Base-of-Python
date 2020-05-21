from sys import argv


def salary(work_hours1, coefficient_hour1, prize1):
    print(f'Итого зарплаты: {work_hours1 * coefficient_hour1 + prize1}')


work_hours = int(argv[1])
coefficient_hour = int(argv[2])
prize = int(argv[3])
salary(work_hours, coefficient_hour, prize)
