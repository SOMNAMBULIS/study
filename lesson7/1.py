"""
Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
Выдать средний бал ученика.
"""
i = ''
grade = []
while i != '0':
	i = input('Enter grade: ') or '0'
	grade.append(int(i))
aver = (sum(grade[:-1]) / len(grade[:-1])) if len(grade)>1 else 0
print(f'Average: {aver:.2f}' )
