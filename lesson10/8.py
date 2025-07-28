"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

* сделать настраиваемы параметр который определяет печать в консоль или в файл
и если в файл передать название фала
"""
def decor(console: bool = True, file_name: str ='error.txt'):
	def decorator(func):
		def wrapper(*args,**kwargs):
			try:
				return func(*args,**kwargs)
			except Exception as ex:
				if console:
					print(func.__name__)
				else:
					with open(file_name, 'a', encoding='utf-8') as f:
						f.write(ex + '/n')
		return wrapper
	return decorator
		
def decorator(func, console: bool = True, file_name: str ='error.txt'):
	def wrapper(*args,**kwargs):
		try:
			return func(*args,**kwargs)
		except Exception as ex:
			if console:
				print(func.__name__)
			else:
				with open(file_name, 'a', encoding='utf-8') as f:
					f.write(ex + '/n')
	return wrapper

@decorator()
def bad_test():
	return 2/0
		
def main():
	bad_test()
		
if __name__ == '__main__':
	main()
