"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
а возвращает список из Yes или No для каждого элемента, 
Yes - если число уже встречалось и No, если нет
[1,2,3,1,4] => [no, no, no, yes, no]

если в списке не все целые числа вернуть False.

"""
def yes_or_no(s:list)->[list|bool]:
	if any([not isinstance(i, int) for i in s]):
		return False
	samp = []
	rez = []
	for i in s:
		if i in samp:
			rez.append('yes')
		else:
			rez.append('no')
			samp.append(i)
	return rez
	
def main():
	l = [1,2,3,1,4]
	print(yes_or_no(l))

if __name__ == '__main__':
	main()
