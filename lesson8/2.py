'''
Написать функцию которая принимает 2 стороны прямоугольника 
и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.

'''
def rectangle(a:[int,float], b:[int,float], square:bool=False) -> float:
	return a*b if square else a+b

def main():
	try:
		param = [input(f'Enter {i}: ') for i in ['a','b','param(0 or any num)']]
		print(rectangle(float(param[0]),float(param[1]),int(param[2])))
	except:
		print('Не верный формат')
	
	
if __name__ == '__main__':
	main()
