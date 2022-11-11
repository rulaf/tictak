import random


def print_hello():
    print('Игра в крестики нолики с ботом!')
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
    print(f'''                    ИГРА            ШАБЛОН
                 {table_temp[0]} | {table_temp[1]} | {table_temp[2]}      | 1 | 2 | 3 |
                 {table_temp[3]} | {table_temp[4]} | {table_temp[5]}      | 4 | 5 | 6 |
                 {table_temp[6]} | {table_temp[7]} | {table_temp[8]}      | 7 | 8 | 9 |
                ''')


def gaming_step():
    '''Ход игрока.'''
    key = input(f'Введите число от 1 до 9 в соответствии с шаблоном  в правой таблице "X": ')
    while key not in map(str, ([i for i in range(1, 10)])) or table_temp[int(key) - 1] != '-':
        key = input(f'Ставить только в пустое место и только от 1 до 9: ')
    key = int(key)
    table_temp[key - 1] = 'X'
    '''Ход бота.'''
    key_bot = random.randint(1, 9)
    while table_temp[int(key_bot) - 1] != '-':
        key_bot = random.randint(1, 9)
    table_temp[key_bot - 1] = '0'


def win_detect():
    for i in winner:
        if table_temp[i[0]] == table_temp[i[1]] == table_temp[i[2]] == 'X':
            print('Вы победили, поздравляем')
            exit()
        if table_temp[i[0]] == table_temp[i[1]] == table_temp[i[2]] == '0':
            print('Победил компьютер, не расстраивайтесь')


# Алгоритм игры
def main():
    counter = 0
    while True:
        counter += 1
        gaming_table()
        gaming_step()
        win_detect()

        if counter == 9:
            print('Ничья')


main()
