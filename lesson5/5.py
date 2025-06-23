"""
Запросить фразу 
    - вывести на экран количество уникальных символов
    - вывести на экран количество уникальных слов
    -* вывести символ который встречался чаще всего

"""
l = input('Enter a string: ').lower()
print('Count char: ',len(set(l)))
print('Count words:',len(set(l.split())))
print('Popular char: ',list(x for x in set(l) if l.count(x) == max(map(l.count,set(l)))))
