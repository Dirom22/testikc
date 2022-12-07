import requests
from datetime import datetime
from threading import Thread

a = ['http://github.ru', 'http://yahoo.com/post', 'http://1plitka-spb.ru//post' , 'http://google.ru/post', 'http://ru.wikipedia.org/post']

def get_html(link):
	for i in range(len(a)):
		link = requests.get(a[i])
		print(link.url)
	

t1 = datetime.now()

for i in range(len(a)):
	response = requests.get(a[i])
	print(response.url)

print('time ', 'Секунд: ', (datetime.now() - t1).seconds, 'Микросекунд: ', (datetime.now() - t1).microseconds)

threads = [Thread(target = get_html, args=(i +1, ))]

t2 = datetime.now()

for t in threads:
	t.start()

for t in threads:
	t.join()

print('time ', 'Секунд: ', (datetime.now() - t2).seconds, 'Микросекунд: ', (datetime.now() - t2).microseconds)