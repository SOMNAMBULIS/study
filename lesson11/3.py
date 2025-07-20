"""

Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты(свойства):
    - value - текущее значение счетчика
    ...

Определить методы:
    - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
    - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
    - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
    - reset, сбрасывает значение счетчика на стартовое    
    - метод __iter__
    - метод __next__
    
    * - stat, возвращает среднее количество изменений счетчика в секунду

"""
class Counter:
	def __init__(self, value:int=0, min_value:int=0, max_value:int=20):
		self.value = value
		self.min_value = min_value
		self.max_value = max_value
		self._reset = value

	def increase(self, count:int=1)->None:
		self.value+=count
		if max_value<self.value<min_value:
			raise StopIteration 
	
	def decrease(self,count:int=1)->None:
		self.value-=count
		if max_value<self.value<min_value:
			raise StopIteration 
	
	def reset(self):
		self.value = self._reset
	
	def __iter__(self):
		pass
		#return iter(i for i in range(self.value, self.max_value))
		
	def __next__(self):
		if self.value > self.max_value:
			raise StopIteration
		self.value+=1
		return self.value
		
	def __str__(self):
		return str(self.value)

def main():
	a = Counter(5,3,10)
	print(next(a))
	a.reset()
	print(a)
	
if __name__ == '__main__':
	main()
		
