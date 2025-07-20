"""
Написать функцию счетчик которая с помощью замыкания (без глобальных переменных)
будет хранить в себе количество запусков и каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def counter(count:int):
	count = count
	def a():
		nonlocal count
		count +=1
		return count
	return a

def main():
	c1 = counter(1)
	c10 = counter(10)
	print('\n'.join(str(c1()) for _ in range(3)))
	print('\n'.join(str(c10()) for _ in range(3)))

if __name__ == '__main__':
	main()
