'''
Запросить число от 1 до 12. 
Если ввели другое число сообщить об ошибке. 
Если ввели не число сообщить об ошибке. 
Когда введут допустимое число - вывести на экран соответствующее 
название месяца, пору года и сколько дней в данном месяце.

'''
num = input('Enter num: ') or ''

db = {1:{'name': 'January', 'ty' : 'Winter', 'day' : '31'},
	2:{'name': 'February', 'ty' : 'Winter', 'day' : '28'},
	3:{'name': 'March', 'ty' : 'Spring', 'day' : '31'},
	4:{'name': 'April', 'ty' : 'Spring', 'day' : '30'},
	5:{'name': 'May', 'ty' : 'Spring', 'day' : '31'},
	6:{'name': 'June', 'ty' : 'Summer', 'day' : '30'},
	7:{'name': 'July', 'ty' : 'Summer', 'day' : '31'},
	8:{'name': 'August', 'ty' : 'Summer', 'day' : '31'},
	9:{'name': 'September', 'ty' : 'Autumn', 'day' : '30'},
	10:{'name': 'October', 'ty' : 'Autumn', 'day' : '31'},
	11:{'name': 'November', 'ty' : 'Autumn', 'day' : '30'},
	12:{'name': 'December', 'ty' : 'Winter', 'day' : '30'}}

if not num.isdigit():
	print('Not number')
elif 0 < int(num) < 13: 
	print(f'Name {db[int(num)]['name']}, tyme of year {db[int(num)]['ty']}, days {db[int(num)]['day']}')
else:
	print('Out of bounds')
	
