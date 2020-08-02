while(True):
    file=open("path.txt","r")
    a=file.read()
    file.close()
    while(a==''):
        file=open("intial.txt","r")
        a=file.read()
        file.close()
        file=open("final.txt","r")
        b=file.read()
        file.close()
        if (a!='' and b!=''):
            a=[int(x) for x in a.split(' ')]
            b=[int(x) for x in b.split(' ')]
            if(a!=b):
                print("-----------------------------------------")
                print("Intial\tFinal")
                print(a,end=" ")
                print(b)
                print(" ")
                c=abs(a[0]-b[0])
                d=a.copy()
                e=abs(a[1]-b[1])
                r=[]
                print("Path co-ordinates:")
                for i in range(0,c):
                    if(b[0]-a[0]>0):
                        d[0]+=1
                        print([d[0],d[1]],end=" ")
                        r.append("1")
                    if(b[0]-a[0]<0):
                        d[0]-=1
                        print([d[0],d[1]],end=" ")
                        r.append("2")
                if(a[1]-b[1]!=0):
                    r.append("3")
                    for i in range(0,e):
                        if(b[1]-a[1]>0):
                            d[1]+=1
                            print([d[0],d[1]],end=" ")
                            r.append("1")
                        if(b[1]-a[1]<0):
                            d[1]-=1
                            print([d[0],d[1]],end=" ")
                            r.append("2")
                    r.append("4")
                print("")
                print("-----------------------------------------")
                file=open("path.txt","w+")
                a=file.read()
                r.reverse()
                z=" ".join(str(x) for x in r)
                file.write(z) 
                file.close()
                file=open("intial.txt","w+")
                a=file.read()
                z=" ".join(str(x) for x in b)
                file.write(z) 
                file.close()
