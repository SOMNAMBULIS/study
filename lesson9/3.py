
'''
Написать рекурсивную функцию, которая принимает 2 аргумента 
(целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
Пример: a = 3, b = 5 -> 12 (3+4+5)
Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)"

'''
# or
# print(sum(i for i in range(int(input()),int(input())+1)))


def recur(a:int, b:int)->int:
	a, b = min(a, b), max(a, b)
	return b + (recur(a, b - 1)) if b > a else a 
	

def main():
	try:
		a, b = [int(input(f'Введите число {i}: ')) for i in 'ab']
		print(recur(a, b))
	except:
		print('Не верный формат')

if __name__ == '__main__':
	main()
