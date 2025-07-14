
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""

def factorial():
	a, i = 1, 1
	while True:
		yield i
		i=i*(a+1)
		a+=1

def main():
	factorial_gen = factorial()
	for _ in range(int(input('Enter num:'))):
		print(next(factorial_gen))
	
if __name__ == '__main__':
	main()
