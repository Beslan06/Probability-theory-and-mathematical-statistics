if __name__ == '__main__':

    # Проведите тест гипотезы. Продавец утверждает, что средний вес пачки
    # печенья составляет 200 г. Из партии извлечена выборка из 10 пачек.
    # Вес каждой пачки составляет:
    # 202, 203, 199, 197, 195, 201, 200, 204, 194, 190.
    # Известно, что их веса распределены нормально. Верно ли утверждение
    # продавца, если учитывать, что доверительная вероятность равна 99%?
    # (Провести двусторонний тест.)
    
    print('mean = 198.5\n' +
          'cn = 4.45\n' +
          'tt = 3.2498\n' +
          'tn = (x-m)/(cn/sqrt(n)) = (198.5-200.0)/(4.45/(10**0.5)) = ' +
          f'{(198.5 - 200.0) / (4.45 / (10**0.5))}\n' +
          'Так как tn < tt гипотеза Н0 верна')


# Чтобы проверить гипотезу, мы можем использовать двусторонний t-критерий. Нулевая гипотеза состоит в том, что средний вес упаковки печенья составляет 200 граммов, 
# а альтернативная гипотеза состоит в том, что средний вес не равен 200 граммам. Мы можем рассчитать t-статистику и p-значение, чтобы определить, 
# отвергаем мы или не отвергаем нулевую гипотезу.

# Предполагая уровень достоверности 99%, мы можем использовать критическое значение 2,821 из таблицы t-распределения с 9 степенями свободы (10 выборок - 1). 
# Если рассчитанная t-статистика больше 2,821 или меньше -2,821, мы отклоняем нулевую гипотезу.

# В этом случае средний вес образца составляет 198 граммов, а стандартное отклонение образца составляет 4,24 грамма. 
# Т-статистика рассчитывается как -5,79, что значительно ниже критического значения -2,821.

# Поэтому мы отвергаем нулевую гипотезу и делаем вывод, что средний вес упаковки печенья не равен 200 граммам с достоверностью 99%.