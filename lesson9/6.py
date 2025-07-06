"""
Дан словарь наблюдения за температурой 
{"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
Отсортировать словарь по температуре в порядке возрастания и обратно.

"""


def sort_dict(d:dict,reverse:bool=False)->dict:
    return dict(sorted(d.items(),key = lambda x:x[1],reverse = True)) if reverse else dict(sorted(d.items(),key = lambda x:x[1]))

def main():
    d = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}
    print(sort_dict(d),sort_dict(d,True),sep='\n')

if __name__ == '__main__':
    main()