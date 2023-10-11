'''
Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
'''


num = int(input('Enter num: '))
if num == 0:
    print(f'Шестнадцатеричное представление числа: ')
    print(f'Проверка результата: {hex(num)}')
else:
    if num != 0 and num <= 255:
        sector_1 = divmod(num, 16)
        fin_hex_list = list(sector_1)
    elif 255 < num < 65536:
        sector_1 = divmod(num, 4096)
        sector_2 = divmod(sector_1[1], 256)
        sector_3 = divmod(sector_2[1], 16)
        sector_4 = divmod(sector_3[1], 1)
        hex_list = list(sector_1 + sector_2 + sector_3 + sector_4)
        fin_hex_list = []
        for i in range(len(hex_list)):
            if i % 2 == 0:
                fin_hex_list.append(hex_list[i])
    elif 65535 < num < 1048578:
        sector_1 = divmod(num, 65536)
        sector_2 = divmod(sector_1[1], 4096)
        sector_3 = divmod(sector_2[1], 256)
        sector_4 = divmod(sector_3[1], 16)
        sector_5 = divmod(sector_4[1], 1)
        hex_list = list(sector_1 + sector_2 + sector_3 + sector_4 + sector_5)
        fin_hex_list = []
        for i in range(len(hex_list)):
            if i % 2 == 0:
                fin_hex_list.append(hex_list[i])

    fin_hex_num = ""
    for i in fin_hex_list:
        if i == 10:
            i = "A"
        elif i == 11:
            i = "B"
        elif i == 12:
            i = "C"
        elif i == 13:
            i = "D"
        elif i == 14:
            i = "E"
        elif i == 15:
            i = "F"
        fin_hex_num += str(i)

    print(f'Шестнадцатеричное представление числа: {fin_hex_num}')
    print(f'Проверка результата: {hex(num)}')
