import subprocess as sp

class DownloadController():
	def __init__(self, threadsCount, picturesCount):
		self.__threadsCount = threadsCount
		self.__picturesCount = picturesCount
		self.__threadValue = 0
		self.__threads = []

	def start(self):
		#создание потоков и распределение задач между ними
		for i in range(4):
			self.__threadValue = round(self.__threadsCount / (4 - i))
			#создание подпроцесса для использования большего количество ресурсов ЦП
			self.__threads.append(sp.Popen('python DownloadThread.py %d %d' 
					% (self.__threadValue, self.__picturesCount // 4), shell = True)) 
			self.__threadsCount -= self.__threadValue

		del i
		self.__clearVariables()

	def __clearVariables(self): #очистка от ненужных переменных
		del self.__threadsCount 
		del self.__threadValue
		del self.__picturesCount

	def stop(self): #остановка всех подпроцессов
		for thread in self.__threads:
			thread.kill()

		del self.__threads, thread

