"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""
def decorator(func):
	def wrapper():
		res = func()
		return res
	return wrapper

def decorator2(func):
	def wrapper(*args,**kwargs):
		try:
			res = func(*args,**kwargs)
			return res
		except Exception:
			print(func.__name__) 
	return wrapper

@decorator2
@decorator	
def bad_test():
	return 2/0
		
def main():
	bad_test()
		
if __name__ == '__main__':
	main()
