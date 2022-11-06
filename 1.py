import json




def add_data(log, passwd):
	with open('log2.json', 'r') as f:
		data = json.load(f)
	if log not in data.keys():
		data[log] = passwd
		with open('log2.json', 'w') as f:
				json.dump(data, f)
		print('регистрация прошла успешно!')
	else:
		print('Логин занят, придумайте другой')
			

def or_data(log, passwd):
	with open('log2.json', 'r') as f:
		data = json.load(f)	
	if log in data.keys():
		if data[log] == passwd:
				print('Вход выполнен, поздравляем!!!')

while True:
	c = input('Вход v,  регистрация r, выход q: ')
	if c == 'q':
		break
	elif c == 'v':
		or_data(input('log: '), input('passwd: '))
	elif c == 'r':
		add_data(input('log: '), input('passwd: '))
	else:
		print('Введите  v, r, q')
		
		