import random


def print_hello():
    # Приветствие
    print('Игра в крестики нолики с компьютером!')
    print('Вы играете за крестики - Х')
    print('Чтобы сделать ход введите число от 1 до 9   ')
    print('в соответствии с шаблоном  в правой таблице ')


# Данные  игры
table_temp = [
    '-', '-', '-',
    '-', '-', '-',
    '-', '-', '-'
]
# Выигрышные комбинации
winner = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
]


def gaming_table():
    # Печать текушей игровой таблицы и шаблона
    print(f'''                    ИГРА            ШАБЛОН
                 {table_temp[0]} | {table_temp[1]} | {table_temp[2]}      | 1 | 2 | 3 |
                 {table_temp[3]} | {table_temp[4]} | {table_temp[5]}      | 4 | 5 | 6 |
                 {table_temp[6]} | {table_temp[7]} | {table_temp[8]}      | 7 | 8 | 9 |
                ''')


def gaming_step():
    # Ход игрока
    key = input(f'Введите число от 1 до 9 в соответствии с шаблоном  в правой таблице "X": ')
    while key not in map(str, ([i for i in range(1, 10)])) or table_temp[int(key) - 1] != '-':
        key = input(f'Ставить крестик только в свободное место и вводить числа только от 1 до 9: ')
    key = int(key)
    table_temp[key - 1] = 'X'
    print('После вашего хода')
    gaming_table()
    win_detect()
    # Ход бота
    if '-' not in table_temp:
        print('Ничья')
        exit()
    key_bot = random.randint(1, 9)
    while table_temp[int(key_bot) - 1] != '-':
        key_bot = random.randint(1, 9)
    table_temp[key_bot - 1] = '0'
    print('После хода компьютера')
    gaming_table()
    win_detect()


def win_detect():
    # Определение победителя
    for i in winner:
        if table_temp[i[0]] == table_temp[i[1]] == table_temp[i[2]] == 'X':
            print('Вы победили, поздравляем')
            exit()
        if table_temp[i[0]] == table_temp[i[1]] == table_temp[i[2]] == '0':
            print('Победил компьютер, не расстраивайтесь')
            exit()


def main():
    while True:
        gaming_step()


print_hello()
gaming_table()
main()
