'''
Дан список содержащий в себе различные типы данных, отфильтровать таким
образом, чтобы 
 - остались только строки.
 - остался только логический тип.
 
'''
def filter_list(l:list)->list:
	return filter(lambda x:isinstance(x,str|bool),l)
    #return [i for i in l if isinstance(i,str|bool)]

def main():
    l =[1,'123',3,4,True,[],False,'qwert']
    print(*filter_list(l))

if __name__ == '__main__':
    main()
