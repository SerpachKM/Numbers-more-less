while True:
        a = int (input('Введите число 1 - '))
        b = int (input('Введите число 2 - '))
        if a == b:
            print('Числа равны')

        elif a < b:
            print(a, 'Меньше' ,b)

        if a > b:
            print(a, 'Больше', b)

        c = (input('Хотите продолжить да или нет: '))

        if c == 'да':
            print('Хорошо заново')
            continue

        if c == 'нет':
            print('Тогда пока')
            break