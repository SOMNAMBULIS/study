"""
Написать функцию которая принимает строку в которой есть 
круглые скобки и возвращает True или False анализируя все ли скобки 
являются закрытыми и расставлены в правильном порядке.
Примеры:
    (()()) -> True
    (()()() -> False
    (hello(2)ver()(33)python) -> True
    (hello(2()ver(33)python)) -> True
    (hello(2()ver(33)python) -> False

"""
def valid(string:str)->bool:
	s = 0
	for i in string:
		if s < 0:
			return False
		if i == '(':
			s+=1
		elif i == ')':
			s-=1
	return s == 0

def main():
	print(valid('(hello(2()ver(33)python)'))

if __name__ == '__main__':
	main()  
