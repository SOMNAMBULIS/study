'''
Запросить высоту елочки - число от 3 до 20. 
Напечатать на экране елочку где ее высота равна числу строк. 
Пример елочки из 4 строк:
   *
  ***
 *****
*******



* - елочка со снегом
'''
import random

num = 0
while num > 20 or num < 3 :
	num = int(input('Enter 2 < num < 21: ') or 0)
l = '\n'.join(('*'*(i*2-1)).center(num*2-1) for i in range(1,num+1))
i = 0
while i < num:
	snow = random.randint(0,len(l)-1)
	if l[snow] == ' ':
		l = l[:snow] + '.'+ l[snow+1:] 
		i+=1
print(l) 
