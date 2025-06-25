'''
Запросить 3 числа. Вывести наибольшее  из них. Решить используя if.
'''
a, b, c = list(map(int,input('Enter 3 num: ').split())) or [0, 0, 0]
m = a if b <= a >= c else b if a <= b >= c else c
print('Max:', m)
