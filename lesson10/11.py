'''
1.Открыть и обработать файл students_grades.txt.
2.Собрать все данные в словарь ниже приведенного формата.
3.Записать в файл "excellent_students.txt" учеников из каждого класса с наибольшим балом.
{
    "9A":[
        {'fio':'fio', 
         'objects':{
            'mathematics':[4, 9, 7],
            'physics':[8, 9, 8, 6],
            ...:...
            }
        },
        ...        
    ],
    "9Б":[
        ...
    ]
}

'''
def dt(name_file:str)->list:
	dt = [] 
	with open(name_file, 'r', encoding='utf-8') as f:
		for i in f.readlines():
			dt.append(i[:-1])
	return dt

def parse(l:list)->dict:
	#lessons = dict()
	for i in l:
		fio = i.split(',')[0]
		clas = i.split(',')[1][1:]
		#lessons = [i[0].split(', ')[-1] for i in l.split('(')]
		# , (''.join(i.split(',')[2:]).split(')').split('(')[1].replace(' ', ','))
		
		lessons = (''.join(i.split(',')[2:]).split(')').split('(')[0][1:-1])
		print(lessons)

def main():
	name_file = 'students_grades.txt'
	#print(dt(name_file))
	parse(dt(name_file))

if __name__ == '__main__':
	main()
