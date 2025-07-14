"""
Создать класс Student.


Определить атрибуты:
    - surname - фамилия
    - name - имя
    - group - номер группы
    - grads - список оценок

Определить методы:
    - инициализатор __init__
    - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
    студентов по среднему баллу
    - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
    - метод average_grade -считает и возвращает среднюю оценку ученика

Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 8
"""
class Student:
	def __init__(self, surname:str, name:str, group:str, grads:list=[]):
		self.surname = surname
		self.name = name
		self.group = group
		self.grads = grads
		
	def __eq__(self, other_obj):
		return self.average_grade() == other_obj.average_grade()
	
	def __ne__(self, other_obj):
		return self.average_grade() != other_obj.average_grade()
	
	def __lt__(self, other_obj):
		return self.average_grade() < other_obj.average_grade()
		
	def __le__(self, other_obj):
		return self.average_grade() <= other_obj.average_grade() 

	def __gt__(self, other_obj):
		return self.average_grade() > other_obj.average_grade()
	
	def __ge__(self, other_obj):
		return self.average_grade() >= other_obj.average_grade()

	def __str__(self):
		return f'{self.surname} {self.name}, {self.group}, отметки: {self.grads}, средний бал: {self.average_grade()}'

	def add_grade(self, *grads:tuple)->None:
		try:
			if not all(0<i<11 for i in grads):
				raise TypeError('Отметки должны быть в диапазоне от 1 до 10')
			[self.grads.append(i) for i in grads]
		except TypeError as ex:
			print(ex)
	
	def average_grade(self):
		return round(sum(self.grads)/len(self.grads), 2)
		
def main():
	students_dt = [['Иванов',"Иван","Группа 1", [4,5,6]],
				['Петров',"Петр","Группа 2", [5,8,6,5]],
				['Сергеев',"Сергей","Группа 3", [6,5,6]],
				['Алексеев',"Алексей","Группа 4", [7,8,9,9]],
				['Васильев',"Василий","Группа 5", [10,7,9,8]]]
	students = []
	for i in students_dt:
		students.append(Student(i[0],i[1],i[2],i[3]))
	
	students[0].add_grade(8,9,9,10)
	print(f'Отсортированный список:',*sorted(students),
		  f'Отфильтрованный список:',
		  *filter(lambda x:x.average_grade()>8,students),sep='\n')
	
if __name__ == '__main__':
	main()
