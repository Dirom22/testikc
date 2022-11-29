import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
	time.sleep(1)
	print(f'аргумент {thread_name} получен')

gtr = [Thread(target = get_thread, args=(arg + 1, )) for arg in range(5)]

t2 = datetime.now()

for b in gtr:
	b.start()

for t in gtr:
	t.join()

print('time ', (datetime.now() - t2).microseconds)
print('*' * 5)

t1 = datetime.now()

for arg in range(5):
	get_thread(arg + 1)

print('time ', (datetime.now() - t1).microseconds)