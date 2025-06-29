"""
1. Запросить у пользователей имя и отзыв о магазине. 
Программа должна запрашивать данные пока не введено слово "stop". 
Все данные сложить в словарь.
    -распечатать количество отзывов
    -распечатать отдельно имена пользователей
    -распечатать отдельно отзывы

"""
i = [(input('Enter name or stop: ') or 'stop', input('Enter review: '))]
d = {}
while i[0][0].lower() != 'stop':
	d |= (i)
	i = [(input('Enter name or stop: ') or 'stop', input('Enter review: '))]
print(f'''Count review: {len(d)} \
		\nNames: {', '.join(d.keys())} \
		\nReview: {', '.join(d.values())}''')

