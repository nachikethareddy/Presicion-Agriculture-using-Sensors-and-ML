import time
file=open("roverstatus.txt","r")
a=int(file.read())
file.close()
while(True):
    file=open("roverstatus.txt","r")
    b=file.read()
    file.close()
    if not b=='':
        if(int(b)>a):
            a=int(b)
            file=open("c:/xampp/htdocs/rover.txt","w+")
            file.write('Online')
            file.close()
        else:
            file=open("c:/xampp/htdocs/rover.txt","w+")
            file.write('Offline')
            file.close()
        time.sleep(12)
