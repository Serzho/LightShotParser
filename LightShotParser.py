import sys
import DownloadController as DC

if len(sys.argv) != 1: #проеврка заданы ли аргументы при запуске 
    assert len(sys.argv) == 3, 'Wrong arguments: must be two arguments' #проверка количества аргументов
    assert sys.argv[1].isdigit() and sys.argv[2].isdigit(), 'Wrong arguments: both arguments might be integer' #проверка типа аргументов
    countPictures, countThreads = map(int, sys.argv[1:])
else: #если аргументы не были заданы
    countPictures = int(input('Please, input count of pictures \n'))
    countThreads = int(input('\nPlease, input count of threads \n'))

print('Starting...')
downloadController = DC.DownloadController(countThreads, countPictures) #создание контроллера потоков загрузки
downloadController.start() #запуск

del countThreads, countPictures


try:
    while True:
        pass
except KeyboardInterrupt:
    print('Stopping...')
    downloadController.stop()
    print('Stooped')

