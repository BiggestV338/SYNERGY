#группа: Pyth-p-Ap-62402/7МОп
#Степанов Владимир Викторович
#GitHub: BiggestV338/SYNERGY synergy

#Урок №5. Логические и условные операторы

#Задание 1.

z = int(input('Введите целое число: '))
if ( z < 0 ) and ( z % 2 == 0 ):
    print(f'{z} отрицательное четное число')
elif z == 0:
    print(f'{z} нулевое число')
elif ( z > 0 ) and ( z % 2 == 0 ):
    print(f'{z} положительное четное число')
else:
    print(f'{z} число не является четным')
#end

#Задание 2.

strng = input('Введите слово: ').lower().strip()

count = 0
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for i in range( len(strng) ):
    if strng[i] == 'a':
        count_a += 1
    elif strng[i] == 'e':
        count_e += 1
    elif strng[i] == 'i':
        count_i += 1
    elif strng[i] == 'o':
        count_o += 1
    elif strng[i] == 'u':
        count_u += 1
    else:
        count += 1

if count > 0:
    print(f'В слове {strng} согласных букв {count}.')
else:
    print(f'В слове {strng} согласных букв нет.')
sum_count = count_a + count_e + count_i + count_o + count_u
if sum_count > 0:
    print(f'В слове {strng} гласных букв {sum_count}.')
else:
    print(f'В слове {strng} гласных букв нет.')
if count_a > 0:
    print(f'В слове {strng} гласной буквы а {count_a}.')
else:
    print(f'В слове {strng} гласной буквы а False.')
if count_e > 0:
    print(f'В слове {strng} гласной буквы e {count_e}.')
else:
    print(f'В слове {strng} гласной буквы e False.')
if count_i > 0:
    print(f'В слове {strng} гласной буквы i {count_i}.')
else:
    print(f'В слове {strng} гласной буквы i False.')
if count_o > 0:
    print(f'В слове {strng} гласной буквы o {count_o}.')
else:
    print(f'В слове {strng} гласной буквы o False.')
if count_u > 0:
    print(f'В слове {strng} гласной буквы u {count_u}.')
else:
    print(f'В слове {strng} гласной буквы u False.')
#end

#Задание 3.

count_x = int(input('Введите минимальную сумму инвестиции: '))
count_a = int(input('Введите имеющуюся сумму у Майкла: '))
count_b = int(input('Введите имеющуюся сумму у Ивана: '))
if ( count_a >= count_x ) and ( count_b >= count_x ):
    #print('Инвестировать могут 2')
    print(2)
elif (( count_a >= count_x ) and ( count_b < count_x )) or (( count_a < count_x ) and ( count_b >= count_x )) or (( count_a < count_x ) and ( count_b < count_x ) and ( count_a + count_b >= count_x )):
    #print('Инвестировать может 1 или хватает вместе')
    print(1)
else:
    #print('Инвестировать не могут')
    print(0)
#end
