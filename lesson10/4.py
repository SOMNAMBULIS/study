"""
Написать генератор последовательности Фибоначчи, 
который принимает максимальное количество чисел в последовательности 
из чисел Фибоначчи и генерирует последовательность. 
Затем  вывести на экран элементы данного генератора. 
Фибоначчи последовательность - первые два числа которой являются 0 и 1, 
а каждое последующее за ними число является суммой двух предыдущих. 
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 и так далее.  
"""

def fib(count:int):
	a, b = 0, 1
	for i in range(count):
		yield a
		a, b = b, a+b

def main():
	count = int(input('Enter num: '))
	print(*fib(count))
	
if __name__ == '__main__':
	main()
