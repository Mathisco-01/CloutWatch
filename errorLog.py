import time
import os



def log(e):
	while False:
		path = os.path.join(os.getcwd(), 'Docs/errors.txt')
		print(os.getcwd())
		f = open(path, 'w')
		f.writeline(e)
		f.close()