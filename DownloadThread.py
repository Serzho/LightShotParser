import threading
import datetime
import httplib2
import re
import random
import time

class DownloadThread(threading.Thread):
	def __init__(self, count_of_pictures = 0):
		super().__init__()
		daemon = True
		self.__running = False
		self.__count_pictures = count_of_pictures
		self.__current_count = 0
	
	def run(self):	
		getTime = lambda: datetime.datetime.now().strftime("%H:%M")
		print('Download Thread was started at %s' % getTime())
		print('%d pictures will be download' % self.__count_pictures)
		print('Starting...')

		self.__running = True

		page_urls = self.__newUrls()
		domain = 'https://prnt.sc/'

		while self.__running:
			print('New one hundred urls...')
			duration = time.time()
			for url in page_urls:
				if(self.__current_count >= self.__count_pictures or
											 not self.__running):
					self.__running = False
					break

				page = self.__getPage(domain + url)
				image_url = self.__getImage(page)
				#print('Ended treatment of', url)

			page_urls = self.__newUrls()
			print('It was checked in %f seconds' % round(time.time() - duration, 3))
					

		print('Download Thread was stopted at %s' % getTime())


	def stop(self):
		self.__running = False
		self.join()

	def __getImage(self, page):
		pattern = r"([\w\.-]+)(\.(jpg)|(png))"

		image_name = re.search(pattern, str(page)).group()
		#print(image_name)
		badNames = ['footer-logo.png', 'icon_lightshot.png', '0_173a7b_211be8ff.png']
		if image_name not in badNames:
			image_url = 'https://image.prntscr.com/image/' + image_name
			#print(image_url)
			self.__current_count += 1
			image = self.__getPage(image_url)
			image_file = open('download/' + ''.join(image_name), 'wb')
			image_file.write(image)
			image_file.close()


	def __getPage(self, url):
		h = httplib2.Http('.cache')
		content = h.request(url)[1]
		del h

		return content


	def __getSymbols(self):
		symbols = [chr(i) for i in range(97, 123)]

		return symbols

	def __newUrls(self):
		urls = []

		symbols = self.__getSymbols()

		for i in range(100):
			urls.append(''.join([random.choice(symbols) for i in range(6)]))

		return urls


		
