"""HT 14 TASK  # 3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної
 інформації про записи: цитата, автор, інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл"""

import requests
from bs4 import BeautifulSoup
import csv


class Quotes:
	"""Клас збирає інформацію з сайту цитат та записує інформацію в файл"""
	base_url = "http://quotes.toscrape.com/"
	url = "/page/"
	all_quotes = []

	def get_infornation(self, number_page):
		"""Запит всієї інформації з сайту"""

		element = requests.get(f"{self.base_url}{self.url}{number_page}")
		return element

	def transformation(self):
		"""Розбір отриманої інформації та відбір потрібних категорій (інформація з 10 сторінок)"""

		for page in range(10):
			element = self.get_infornation(page)
			soup = BeautifulSoup(element.text, "html.parser")  # не вдалось встановити бібліотеку lxml спробувати ще раз!!!
			quotes = soup.find_all(class_="quote")
			for quote in quotes:
				self.all_quotes.append({
					"text": quote.find(class_="text").get_text(),
					"author": quote.find(class_="author").get_text(),
					"about author": f'{self.base_url}{quote.find("a")["href"]}'
				})
		return

	def writer(self):
		"""Запис отриманої інформації"""

		with open('basa.csv', 'w') as file:
			writer = csv.DictWriter(
				file, fieldnames=list(self.all_quotes[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
			writer.writeheader()
			for row in self.all_quotes:
				writer.writerow(row)


if __name__ == '__main__':
	quote = Quotes()
	quote.transformation()
	quote.writer()
	print('ok')
