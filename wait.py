a={'p1':"0 0",'p2':"0 1",'p3':"1 0",'p4':"1 1"}
while True:
    file=open("queue.txt","r")
    b=file.read()
    file.close()
    if not b=="":
        b=[str(x) for x in b.split(" ")]
        file=open("intial.txt","r")
        c=file.read()
        file.close()
        d=b.pop(0)
        q=" ".join(str(x) for x in b)
        file=open("queue.txt","w+")
        file.write(q)
        file.close()
        print(d)
        d=a[d]
        file=open("path.txt","r")
        e=file.read()
        file.close()
        if not c==d:
            print("waiting......")
            while True:
                if(e!=""):
                    file=open("path.txt","r")
                    e=file.read()
                    file.close()
                    continue
                else:
                    file=open("final.txt","w+")
                    file.write(d) 
                    file.close()   
                    break
