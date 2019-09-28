'''
На вход алгоритму подаётся строка, содержащая цифры и символы латинского алфавита. Эта строка разбивается на так называемые "серии", которые кодируются парой число-символ или просто символ (в таком случае число считается равным единице). Результат должен содержать эти серии в том же порядке, что они и встречаются в исходной строке, при этом каждая серия раскрывается в последовательность символов соответствующей длины.

Например, рассмотрим строку

3ab4c2CaB
Разобъём её на серии
3a b 4c 2C a B
После чего преобразуем серии и получим исходную закодированную строку:
aaabccccCCaB

'''
import re
coded = input()
def decode_rle(code):
    mul = ''
    string = ''
    for symbol in code:
        if symbol.isdigit():
            mul += symbol
        else:
            string += symbol * int(mul) if mul else symbol
            mul = ''
    return string

print(decode_rle(coded))

n = input()
num = 0
for l in n:
    if not l.isdigit():
        if num == 0:
            print(l, end='')
        else:
            print(l*num, end='')
        num = 0
    else:
        num = num*10 + int(l)

'''
from re import sub
print(sub(r'(\d+)(\w)', lambda m: m.group(2) * int(m.group(1)), input()))
'''

d = ''
for s in input():
  if ~'0123456789'.find(s):
    d += s
  else:
    print(s * int(d or 1), end='')
    d = ''
