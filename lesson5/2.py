"""
2. Создать структуру данных сотрудников фирмы с 
    тремя сотрудниками. каждый сотрудник должен иметь:
        ФИО, 
        должность, 
        год рождения, 
        список навыков, 
        список детей с их именем и годом рождения. 
    
    Запросить ФИО сотрудника и вывести по нему информацию.
"""
l ={
'Иванов Иван Иванович':{'name': 'Иванов Иван Иванович', 'rank':'Водитель', 'year':1975, 'skill': ['Категория А', 'Категория B'], 'child' : [{'name':'Василий', 'year': 2006},{'name':'Сергей', 'year': 2008}]},
'Петров Петр Петрович':{'name': 'Петров Петр Петрович', 'rank':'Программист', 'year':1986, 'skill': ['Python', 'Java', 'C++'], 'child' : [{'name':'Акакий', 'year': 2005},{'name':'Екатерина', 'year': 2010}]},
'Гусева Екатерина Константиновна':{'name': 'Гусева Екатерина Константиновна', 'rank':'Актриса', 'year':1976, 'skill': ['Театр', 'Кино', 'Озвучка'], 'child' : [{'name':'Алексей', 'year': 1998}]},
}
print(l.get(input('ФИО: ').title(),'Нет такого ФИО'))

