'''
Написать рекурсивную функцию, которая вычисляет  
факториал переданного в нее числа.

'''
def factorial(a:int)->int:
	return a * factorial(a-1) if a>1 else 1

def main():
	try:
		num = int(input('Введите число: '))
		print(factorial(num))
	except:
		print('Не верный формат')

if __name__ == '__main__':
	main()
