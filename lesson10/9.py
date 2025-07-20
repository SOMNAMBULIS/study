"""
Написать функцию hello, которая принимает 2 аргумента name и surname и
выводит принтом "Привет, {name} {surname}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""
def log_decorator(func):
	def wrapper(*args, **grwars):
		print(f'Выполняеся функция {func.__name__} с аргусентами  ')
		func(*args, **grwars)
		print(f"{func.__name__} - завершена")
	return wrapper
	
@log_decorator
def hello(name:str,surname:str)->None:
	print(f"Привет, {name} {surname}")

def main():
	hello('Name', 'Surname')
	
if __name__ == '__main__':
	main()
