"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title (len<50), year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""

from datetime import date

CURRENT_YEAR = date.today().year

class BookCard:
	__autrhor = ''
	__title = ''
	__year = 0
	def __init__(self, author:str, title:str, year:int):
		self.author = author
		self.title = title
		self.year = year
	
	@property
	def author(self):
		return self.__author 
	
	@property
	def title(self):
		return self.__title 
	
	@property
	def year(self):
		return self.__year
	
	@author.setter	
	def author(self, val):
		if isinstance(val, str):
			self.__author = val
		else:
			raise ValueError
	
	@title.setter		
	def title(self, val):
		if isinstance(val, str) and len(val)<50:
			self.__title = val
		else:
			raise ValueError
	
	@year.setter		
	def year(self, val):
		if isinstance(val, int) and 0 < val <= CURRENT_YEAR:
			self.__year = val
		else:
			raise ValueError

	def __lt__(self, other_obj):
		return self.__year < other_obj.__year
	
	def __str__(self):
		return f'Author: {self.__author}, Title: {self.__title}, year: {self.__year}' 
		
def main():
	a = [BookCard('Author1','1',1),BookCard('Author2','2',2),BookCard('Author3','3',2)]
	print(*(i for i in a), sep = '\n')
	
if __name__ == '__main__':
	main()
