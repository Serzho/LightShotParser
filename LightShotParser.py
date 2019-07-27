import DownloadThread
import subprocess as sp
import sys


countPictures = int(input('Please, input count of pictures \n'))
countThreads = int(input('\nPlease, input count of threads \n'))


sp.check_call('python download.py %d %d' %
              (countThreads, countPictures), shell = True)

try:
    while True:
        pass
except KeyboardInterrupt:
    print('stooped')

