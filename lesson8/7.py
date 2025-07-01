"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""
from text import text 

def no_regular(s:str)->dict:
	dt = {'count_char' : len(s), 'count_word' : len(s.split()),
		  'count_line' : len(s.split('\n')), 'count_offer' : len(s.split('.'))}
	return dt

def no_regular2(dt:dict)->None:
	print(f'Количество символов: {dt['count_char']},\n\
Количество слов: {dt['count_word']},\n\
Количество строк: {dt['count_line']},\n\
Количество предложений: {dt['count_offer']}')

def main():
	no_regular2(no_regular(text))
	
if __name__ == '__main__':
	main()
