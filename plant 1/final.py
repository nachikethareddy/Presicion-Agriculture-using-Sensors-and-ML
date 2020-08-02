import json
import requests
import csv
import time


sensordata=[]
with open('feeds.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        sensordata.append(row)
moisture=[]
temperature=[]
humidity=[]
a=['created_at','value']
moisture.append(a)
temperature.append(a)
humidity.append(a)
for i in range(1,len(sensordata)):
    q=sensordata[i]
    d=q[0]
    d=d.replace(' ','T',1)
    d=d.replace(' UTC','Z')
    if q[2]!= '':
        if q[2]!= 'nan':
            b=[d,q[2]]
            moisture.append(b)
    elif q[3]!= '':
        if q[3]!= 'nan':
            b=[d,q[3]]
            temperature.append(b)
    elif q[4]!= '':
        if q[4]!= 'nan':
            b=[d,q[4]]
            humidity.append(b)

with open('moisture.csv', mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in moisture:
        writer.writerow(i)
file.close()
with open('temperature.csv', mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in temperature:
        writer.writerow(i)
file.close()
with open('humidity.csv', mode='w',newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in humidity:
        writer.writerow(i)
file.close()


#part2


while True:
        file = open("testfile.txt", "r")
        a=int(file.read())
        file.close()
        r=requests.get("https://api.thingspeak.com/channels/846171/feeds/last?key=CAKRRG8UVYUBEUF0")
        data = r.json()
        i=[]
        i.append(data['created_at'])
        i.append(data['entry_id'])
        i.append(data['field1'])
        i.append(data['field2'])
        i.append(data['field3'])
        file=open("last.txt","r")
        c=file.read()
        file.close()
        c=[str(x) for x in c.split(" ")]
        if(a!=data['entry_id']):
                file = open("C:/xampp/htdocs/server1.txt","w+")
                d='Online'
                file.write(d)
                file.close()
                print('Online')
                print(i)
                if i[2]!= None:
                        b=[i[0],i[2]]
                        c[1]=i[2]
                        file = open("last.txt","w+")
                        d=' '.join(str(x) for x in c)
                        file.write(d)
                        file.close() 
                        with open('moisture.csv', mode='a',newline='') as file:
                                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                writer.writerow(b)
                elif i[3]!= None:
                        b=[i[0],i[3]]
                        c[2]=i[3]
                        file = open("last.txt","w+")
                        d=' '.join(str(x) for x in c)
                        file.write(d)
                        file.close()
                        with open('temperature.csv', mode='a',newline='') as file:
                                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                writer.writerow(b)
                elif i[4]!= None:
                        b=[i[0],i[4]]
                        c[3]=i[4]
                        file = open("last.txt","w+")
                        d=' '.join(str(x) for x in c)
                        file.write(d)
                        file.close()
                        with open('humidity.csv', mode='a',newline='') as file:
                                writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                                writer.writerow(b)
        else:
                print("Offline")
                print(c)
                file = open("C:/xampp/htdocs/server1.txt","w+")
                d='Offline'
                file.write(d)
                file.close()
        file = open("testfile.txt","w") 
        file.write(str(data['entry_id']))
        file.close() 
        time.sleep(17)
