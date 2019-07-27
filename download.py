import subprocess as sp
import sys

#print(sys.argv)

threadsCount, picturesCount  = map(int, sys.argv[1:])

threads = []

for i in range(4):
	threadValue = round(threadsCount / (4 - i))
	threads.append(sp.Popen('python DownloadThread.py %d %d' 
			% (threadValue, picturesCount // 4), shell = True))
	threadsCount -= threadValue

#del threadValue, threadsCount, picturesCount

