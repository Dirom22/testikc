import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

def list(rates_list):

	rates = [float(str(rates_list[i-1])[4: -5]) for i in range(len(rates_list)-1, 3, -3)]
	dates = [str(rates_list[i-2])[6: -5] for i in range(len(rates_list)-1, 3, -3)]
	return dates, rates

def fun():
	
	res = requests.get('http://mfd.ru/currency/?currency=USD')

	suop = BeautifulSoup(res.text, 'html.parser')
	rates = suop.find('table', {'class': 'mfd-table mfd-currency-table'})
	rates_list = rates.find_all('td')
	dates, rates = list(rates_list)

	c, ax = plt.subplots()

	ax.xaxis.set_major_locator(MaxNLocator(6))
	ax.grid() 

	ax.set_xlabel('ДАТА', fontsize=14)
	ax.set_ylabel('RUB', fontsize=14)
	ax.set_title(r'Курс RUB / USD', fontsize=16, y=1.03)
	ax.plot(dates, rates)

	plt.show()

fun()

