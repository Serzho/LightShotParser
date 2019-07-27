import DownloadThread

countPictures = int(input('Please, input count of pictures '))
downThr = DownloadThread.DownloadThread(countPictures)
downThr.start()


try:
    while True:
        pass
except KeyboardInterrupt:
    print('stooped')
    downThr.stop()
