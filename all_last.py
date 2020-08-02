import os
import time
while True:
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, 'plant 1/last.txt')
    file=open(filename,"r")
    a=file.read()
    file.close()
    file=open('record.txt',"w+")
    file.write(a)
    file.close()
    time.sleep(13)
    
