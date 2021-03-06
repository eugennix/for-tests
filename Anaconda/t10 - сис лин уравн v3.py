# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 12:21:10 2019
Даны числа a, b, c, d, e, f.
Решите систему линейных уравнений
ax + by = e
cx + dy = f

Если система не имеет решений,
то программа должна вывести единственное число 0.

Если система имеет бесконечно много решений,
 каждое из которых имеет вид y=px+q,
 то программа должна вывести число 1, а затем значения p и q.

Если система имеет единственное решение (x₀,y₀),
 то программа должна вывести число 2, а затем значения x₀ и y₀.

Если система имеет бесконечно много решений вида x=x₀,
 y — любое, то программа должна вывести число 3, а затем значение x₀.

Если система имеет бесконечно много решений вида y=y₀,
 x — любое, то программа должна вывести число 4, а затем значение y₀.

Если любая пара чисел (x,y) является решением,
 то программа должна вывести число 5.
"""

a, b, c, d, e, f = [float(input()) for _ in range(6)]


def SLAU(a, b, c, d, e, f):
    zero = 1.0e-8
    Dm = a * d - c * b
    Dy = a * f - c * e
    Dx = d * e - b * f

    if abs(Dm) > zero:
        # Одно решение
        x = Dx / Dm
        y = Dy / Dm
        return (2, x, y)
    elif abs(a) + abs(b) + abs(c) + abs(d) <= zero:
        if abs(e) + abs(f) <= zero:
            # бесконечное множество решений
            return [5]
        else:
            # решений нет
            return [0]
    elif abs(Dx) > zero or abs(Dy) > zero:
            # решений нет
            return [0]

    elif abs(b) <= zero:
        if abs(a) > zero:
            return (3, e / a)
        elif abs(d) <= zero:
            return [3, f / c]
        elif abs(c) <= zero:
            return [4, f / d]
        else:
            return [1, -c / d, f / d]

    elif abs(a) <= zero:
        if abs(b) > zero:
            return [4, e / b]
        elif abs(d) <= zero:
            return [3, f / c]
        elif abs(c) <= zero:
            return [4, f / d]
    else:
        return [1, -a / b, e / b]


def trunc0(n):
    sn = str(n).split('.')
    if len(sn) == 2 and sn[1] == '0':
        return sn[0]
    return n

res = SLAU(a, b, c, d, e, f)
if res[0] == 2:
    x = trunc0(res[1])
    y = trunc0(res[2])
    print(x, y)
