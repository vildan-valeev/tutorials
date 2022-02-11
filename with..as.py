"""Менеджеры контекста

Критическая проверка. Если ошибка, то файл закрывается.
"""

with open('test.txt', 'wt', encoding='utf-8') as inFile:
    num = int(input())
    line = str('1/' + str(num) + ' = ' + str(1 / num))
    print(line)
    inFile.write(line)
