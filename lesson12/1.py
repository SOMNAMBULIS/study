"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""
import abc 

class Animal(abc.ABC):
	def __init__(self,name:str=''):
		self.name = name
		
	@abc.abstractmethod
	def says(self):
		pass

class Cat(Animal):
	def says(self):
		print(f'{self.name} - кошка. Говорит МЯУ!')

class Dog(Animal):
	def says(self):
		print(f'{self.name} - собака. Говорит ГАВ!')
		
class Cow(Animal):
	def says(self):
		print(f'{self.name} - корова. Говорит МУ!')
		
def main():
	cat, dog, cow = Cat('Рыжик'), Dog('Жучка'), Cow('Мурка')
	cat.says()
	dog.says()
	cow.says()

if __name__ == '__main__':
	main()

