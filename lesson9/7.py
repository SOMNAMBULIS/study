"""
Дан список пользователей след. формата: 
[{"name":"some_name", "login":"some_login", "password":"some_password" },
 ...
]

Отфильтровать используя функцию filter() список на предмет паролей 
которые менее 5 символов.

*Отфильтровать используя функцию filter() список на предмет валидных логинов. 
Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
Каждому пользователю с плохим логином вывести текст 
"Уважаемый user_name, ваш логин user_login не является корректным."

"""

def login_val(l:list)->list:
	bad_login = filter(lambda x:not x['login'].replace('_','0').isalnum() and x['login'].isascii(),l)
	#bad_login = filter(lambda x:all(True if i.lower() not in 'qwertyuiopasdfghjklzxcvbnm_0123456789' else False for i in x['login']),l)
	for i in bad_login:
		print(f'Уважаемый {i["name"]}, ваш логин {i["login"]} не является корректным.')

def filter_pass(l:list)->list:
    return list(filter(lambda x:len(x['password'])<5,l))

def main():
    d = [
        {"name": "name1", "login": "valid_login", "password": "some_password"},
        {"name": "name2", "login": "some*login", "password": "some"},
        {"name": "name3", "login": "___", "password": "some"},
    ]
    print(*filter_pass(d),sep='\n')
    login_val(d)
    
if __name__ == '__main__':
    main()
