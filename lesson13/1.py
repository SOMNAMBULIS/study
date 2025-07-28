"""
Создать класс User с атрибутами:

Свойства:
	- name - имя - содержит только буквы русского алфавита 
	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
                содержит менее шести символов
                содержит строчную букву
                содержит заглавную букву
                содержит число
	- is_blocked - заблокирован
	- subscription_date - дата до какой действует подписка
	- subscription_mode - вид подписки (free, paid)


Методы:
	- bloc - принимает логическое значение и помечает пользователя заблокированным 
	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
						Если дата не передана значит на дату проверки. 
						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
	- change_pass - смена пароля и присваивание его в качестве действующего. 
						Пароль должен пройти валидацию. 
						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
При изменении даты подписки  вид подписки меняется на платный.
Валидацию данных сделать через регулярные выражения
"""
import re
from datetime import datetime, timedelta
from random import randint, choices
import string

class User:
	def __init__(self, name:str, login:str, password:str = None): 
		self.name = self._valid_name(name)
		self.login = self._valid_login(login)
		self.password = self._valid_password(password) if password else self._gen_password(password)
		self.is_blocked = False
		self.subscription_date = datetime.now() + timedelta(days=30)
		self.subscription_mode = 'free'

	def _valid_name(self, name):
		if not re.match(r'^[А-Яа-яёЁ]+$',name):
			raise TypeError('Имя должно состоять из кириллици')
		return name
	
	def _valid_login(self, login):
		if not re.match(r'^[A-Za-z0-9_]{6,}$',login):
			raise TypeError('Логин должен состоять из латинского алфавита, цифр и _')
		return login
	
	def _valid_password(self, password):
		password = password or ''
		return password if re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{,6}$',password) else self._gen_password(password)
		
	def _gen_password(self,password):
		password = password or ''
		while not re.match(r'^(?=.*[0-9].*)(?=.*[a-z].*)(?=.*[A-Z].*)[0-9a-zA-Z]{,6}$',password):
			password = ''.join(choices(string.ascii_letters + string.digits,k =randint(3,6)))
			
		print(f'Пароль не соответствует критериям сгенерирован новый пароль: {password}')
		return password
	
	def block(self, block:bool):
		self.is_blocked = block
	
	def check_subscr(self, date=None):    
		check_date = date or datetime.now()
		active = check_date <= self.subscription_date
		days_left = (self.subscription_date - check_date).days if active else False
		print(f'active: {active}',
              f'subscription_mode: {self.subscription_mode}',
              f'days_left: {days_left}',sep = '\n')
	
	def chacge_pass(self,password:str = None):
		self.password = self._valid_password(password) if password else self._gen_password(password)
	
	def get_info(self):
		if self.is_blocked:
			print(f'Пользователь {self.name} заблокирован')
		else:
			print(f'Name: {self.name}',
				  f'Login: {self.login}',
				  f'Password: {self.password}',
				  f'Subscription mode: {self.subscription_mode}',
				  f'Subscription_date: {self.subscription_date}',sep = '\n'
				  )
	
	def set_subscription(self, date:str):
		self.subscription_date = datetime.strptime(date, "%Y-%m-%d")
		self.subscription_mode = 'paid'
	
def main():
	try:
		a = User('Имя', 'loggins')
		a.set_subscription('2028-09-12')
		a.get_info()
	except Exception as ex:
		print(ex)
		
if __name__ == '__main__':
	main()

