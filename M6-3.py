import requests
from datetime import datetime
from threading import Thread

a = ['http://github.ru', 'http://yahoo.com/post', 'http://1plitka-spb.ru//post', 'http://google.ru/post', 'http://ru.wikipedia.org/post']

def get_html(link):
	response = requests.get(a[i])
	print(link, len(response.text))
	
t1 = datetime.now()

for i in range(5):
	print(get_html(a[i]))

print('time ', 'Секунд: ', (datetime.now() - t1).seconds, 'Микросекунд: ', (datetime.now() - t1).microseconds)

threads = [Thread(target = get_html, args = [a [i]]) for i in range(5)]

t2 = datetime.now() 

for t in threads:
	t.start()

for t in threads:
	t.join()

print('time ', 'Секунд: ', (datetime.now() - t2).seconds, 'Микросекунд: ', (datetime.now() - t2).microseconds)