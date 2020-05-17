def info_human(name, second_name, email, year_birth, city_life, human_phone):
    print(f' Имя - {name}; Фамилия - {second_name}; год рождения - {year_birth};'
          f' город проживания {city_life}; email - {email}; номер телефона - {human_phone}')


info_human(human_phone=911, city_life='Королев', year_birth=1986,
           email='qwerty@mail.ru', name='Сергей', second_name='Сергеев')