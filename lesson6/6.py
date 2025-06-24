"""
Даны 4 переменные - a1, a2, a3, a4.
1 - вывести True если все они дробные числа
2 - вывести True если одна из них строка
3 - вывести True если  одна пара переменных является целочисленным типом. 
    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"
"""
# не уверен что я правильно понял условия
a1, a2, a3, a4 = 1, 2.5, 2, '5'
print('1 -', all([isinstance(a1, float),isinstance(a2, float),isinstance(a3, float),isinstance(a4, float)]))  
print('2 -',any([isinstance(a1, str),isinstance(a2, str),isinstance(a3, str),isinstance(a4, str)]))
print('3 -', isinstance(a1, int) and isinstance(a3, int) or 
	isinstance(a2, int) and isinstance(a3, int) or 
	isinstance(a3, int) and isinstance(a4, int))
