'''
Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.

'''
# другое решение
#mul = lambda arr:arr[0] * mul(arr[1:]) if arr else 1
#print(mul(range(1,int(input('Enter Num: '))+1)))



class LessThanZero(Exception):
	def __init__(self,err='Число меньше 0'):
		print(err)


def fractal(a:int)->int:
	if a < 0:
		raise LessThanZero
	s = 1
	for i in range(1,a+1):
		s*=i
	return s
		

def main():
	try:
		print(fractal(int(input('Enter num: '))))
	except ValueError:
		print('Не верный формат')
	except LessThanZero:
		pass

if __name__ == '__main__':
	main()
