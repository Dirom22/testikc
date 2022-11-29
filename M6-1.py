import time

def get_thread(thread_name):
	time.sleep(1)
	print(f'аргумент {thread_name} получен')

for arg in range(5):
	get_thread(arg + 1)