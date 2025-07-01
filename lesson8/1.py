"""
Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
а возвращает в виде краткого формата. 
Функция должна содержать необязательный параметр в виде логического значения 
и в зависимости от него возвращала ФИО в двух следующих форматах:
 -  Николаев И.С. 
 -  И.С.Николаев


"""

def name(fio:str, reverse:bool=False) -> str:
	if len(fio.split()) != 3:
		raise TypeError('Не верный формат')
	fio = [fio.split()[0], fio.split()[1][0] + '.', fio.split()[2][0] + '.']
	fio = f'{fio[1]}{fio[2]}{fio[0]}' if reverse else f'{fio[0]} {fio[1]}{fio[2]}'
	return fio		

def main():
	try:
		fio = input('Enter FIO: ') or 'Николаев Игорь Степанович'
		print(name(fio))
		print(name(fio=fio, reverse=True))
	except TypeError as ex:
		print(ex)
	
if __name__ == '__main__':
	main()


