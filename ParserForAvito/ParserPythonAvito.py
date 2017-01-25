# - Parsing avito
# - Created Vecnik88
# - 25.01.2017

# Скрипт парсера на авито, собирает все объявления о продаже автомобилей марки VOLVO
# и сохраняет их в файл компьютера
# можно его подстроить под любой запрос на авито, путем изменения url адреса
# также можно добавить различные другие фильтры, парсить со всех страниц и тд

import requests
from bs4 import BeautifulSoup
import csv

#	### Порядок работы ###

# - посчитать количество страниц
# - сформировать адреса сайтов на страницы выдачи
# - собрать данные

def get_html(url):					# <---. считывает url, возвращает ввиде текста
	r = requests.get(url)
	return r.text					# <---. возвращает html код заданной страницы

###########################################################################################################

def get_total_pages(html):			# <---. определяет количество страниц
	soup = BeautifulSoup(html, 'lxml')

	pages = soup.find('div', class_='pagination-pages').find_all('a',class_='pagination-page')[-1].get('href')
	total_pages = pages.split('=')[1].split('&')[0] 	# <---. делим наш запрос и в конце получаем номер страницы

	return int(total_pages) # <---. возвращает количество страниц по данному запросу

###########################################################################################################

def write_csv(data):
	with open('avito.csv','a') as f:
		writer = csv.writer(f)

		# считываем в файл

		writer.writerow((data['title'],							
						 data['price'],
						 data['metro'],
						 data['url']))

############################################################################################################

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')

	# получаем список всех item_table

	ads = soup.find('div', class_='catalog-list').find_all('div', class_='item_table')

	for ad in ads:
		# title, price, metro, url
		name = ad.find('div', class_='description').find('h3').text.strip().lower()

		 if 'volvo' in name: # <---. если есть вольво в заголовке, то парсим, иначе продолжаем цикл

			try:
				title = ad.find('div', class_='description').find('h3').text.strip()
			except:
				title =''
			try:
				url = 'https://www.avito.ru' + ad.find('div', class_='description').find('h3').find('a').get('href')
			except:
				url =''
			try:
				price = ad.find('div', class_='about').text.strip()
			except:
				price =''
			try:
				metro = ad.find('div', class_'date').find_all('p')[-1].text.strip()
			except:
				metro =''

			data = {'title': title,
					'price': price,
					'metro': metro,
					'url': url}
			write_csv(data)		

		else:
			continue

###########################################################################################################

def main():
	# https://www.avito.ru/moskva/avtomobili?p=1&q=volvo <---. url parsing

	url = https://www.avito.ru/moskva/avtomobili?p=1&q=volvo

	base_url = 'https://www.avito.ru/moskva/avtomobili?' # <---. неизменная часть запроса
	page_part = 'p='    # <---. сюда будем подставлять номер страницы
	query_part = '&q=volvo'  # <---. отвечает за запрос, запрос у нас постоянен

	total_pages = get_total_pages(get_html(url))
	for i in range(1,3): # <---. ограничимся двумя страницами, если нужны все - то до total_pages

		url_gen = base_url + page_part + str(i) + query_part # <---. создаем наш запрос
		# print(url_gen)
		html = get_html(url_gen)
		get_page_data(html)

###########################################################################################################

if __name__ == '__main__': # <---. вызывает ф-цию main
	main()