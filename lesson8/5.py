'''
Написать функцию count_char, которая принимает строковое значение,
из которого создает и возвращает словарь, следующего вида:
{'буква': 'количество-вхождений-в-строку'}
Нельзя пользоваться collections.Counter!

'''
def count_char(a:str)->dict:
	s = set(a)
	dt = {}
	for i in s:
		dt |= [(i, a.count(i))]
	return dt
	
def main():
	st = input('Enter string: ') or 'Какая-то строка'
	print(count_char(st))
	
if __name__ == '__main__':
	main()

