import random
import time

class LotoCard:
    def __init__(self, name):
        self.name = name
        self.list = self.fill_card()

    @staticmethod
    def fill_card():
        card_full_info = []
        for count in range(3):  # формируем 3 линии карточки
            line = []
            for i in range(6):
                while True:
                    el = random.randint(1, 90)
                    if line.count(el) == 0 and card_full_info.count(el) == 0:
                        break
                line.append(el)
            line.sort()
            for count_gap in range(5, 8):  # добавил 3 пропуска в линию для антуража
                position_gap = random.randint(1, count_gap)
                line.insert(position_gap, '  ')
            card_full_info.extend(line)
        return f'{card_full_info}'

    def __str__(self):
        return self.list

    def __getitem__(self, item):
        return self.list[item]


class LotoGame(LotoCard):
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def start(self):

        def redo_line(list_play_fo_work):
            list_player = []
            strit = ""
            count_play = 0
            for i in list_play_fo_work:
                if i.isdigit():
                    strit += i
                elif i == "'":
                    count_play += 1
                    if count_play == 2:
                        list_player.append('  ')
                        count_play = 0
                else:
                    if len(strit) == 0:
                        continue
                    else:
                        list_player.append(int(strit))
                        strit = ''
                    continue
            return list_player

        def beautiful_print(list_player):
            count_el = 0
            line_print = ''
            for i in list_player:
                if len(str(i)) == 1:
                    temp = str(i).ljust(2, ' ')
                    line_print += (temp + ' ')
                else:
                    line_print += (str(i) + ' ')
                count_el += 1
                if count_el == 9:
                    print(line_print)
                    line_print = ''
                    count_el = 0
            return list_player

        list_player_1 = redo_line(self.player_1)
        list_player_2 = redo_line(self.player_2)

        bag_number = [x for x in range(1, 91)]
        random.shuffle(bag_number)
        my = iter(bag_number)

        count_iter = 89
        while True:
            iter_num = next(my)
            print(f'\n{self.player_1.name}:\n{26 * "-"}')
            beautiful_print(list_player_1)
            print(f'\n{self.player_2.name}:\n{26 * "-"}')
            beautiful_print(list_player_2)
            print(f'\nНовый бочонок {iter_num}, осталось {count_iter}')
            answer_user = input('Хотите зачеркнуть? y/n: ')
            if answer_user == 'y' and list_player_1.count(iter_num) == 0:
                print(f'Вы проиграли! У вас не было числа {iter_num}')
                break
            if answer_user == 'n' and list_player_1.count(iter_num) != 0:
                print(f'Вы проиграли! У вас было число {iter_num}')
                break
            if list_player_1.count(iter_num) != 0:
                a = list_player_1.index(iter_num)
                list_player_1.pop(a)
                list_player_1.insert(a, '*')
            if list_player_2.count(iter_num) != 0:
                a = list_player_2.index(iter_num)
                list_player_2.pop(a)
                list_player_2.insert(a, '*')
            win1 = list_player_1.count('*')
            if win1 == 18:
                print('Вы победили! Рандом на вашей стороне!')
                break
            win2 = list_player_2.count('*')
            if win2 == 18:
                print('Победил компьютер! Рандом на стороне PC!')
                break
            count_iter -= 1
            if count_iter == -1:
                break


a = time.time()
human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')
game = LotoGame(human_player, computer_player)
game.start()
b = time.time()
print(f'Вы играли {round(b - a)} сек')