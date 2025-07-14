"""
Написать генератор triangular_numbers, который возвращает подряд 
треугольные числа

Формула:
Tn = 1 / 2 * n * (n + 1)

Например:
tn_gen = triangular_numbers()

next(tn_gen) -> 1
next(tn_gen) -> 3
next(tn_gen) -> 6
next(tn_gen) -> 10
next(tn_gen) -> 15
next(tn_gen) -> 21
"""
def triangular_numbers():
	count = 1
	while True:
		yield 1 / 2 * count * (count + 1)
		count += 1

def main():
	tn_gen = triangular_numbers()
	for _ in range(int(input('Enter num: '))):
		print(int(next(tn_gen)))

if __name__ == '__main__':
	main()
