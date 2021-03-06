d = (int(input()), int(input()), int(input()))
a, b, c = int(input()), int(input()), int(input())
positions = [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]


def capasity(deposit, box):
    n1 = d[0] // box[0]
    n2 = d[1] // box[1]
    n3 = d[2] // box[2]
    return n1 * n2 * n3

print(max(capasity(d, b) for b in positions))
'''
На склад, который имеет форму прямоугольного параллелепипеда, привезли ноутбуки, упакованные в коробки. 
Каждая коробка также имеет форму прямоугольного параллелепипеда. 
По правилам хранения коробки с ноутбуками должны быть размещены на складе с выполнением следующих двух условий:

Стороны коробок должны быть параллельны сторонам склада.
Коробку при помещении на склад разрешается расположить где угодно 
(с выполнением предыдущего условия), в том числе на другой коробке, но все коробки должны быть ориентированы одинаково 
(т.е. нельзя одну коробку расположить “стоя”, а другую —“лежа”)
Напишите программу, которая по размерам склада и размерам коробки с ноутбуком определит 
максимальное количество ноутбуков, которое может быть размещено на складе.

Формат ввода
Программа получает на вход шесть натуральных чисел. Первые три задают длину, высоту и ширину склада. 
Следующие три задают соответственно длину, высоту и ширину коробки с ноутбуком.

Формат вывода
Программа должна вывести одно число — максимальное количество ноутбуков, которое может быть размещено на складе.'''