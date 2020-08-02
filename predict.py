import json
import requests
import time
import numpy as np
import joblib

filename = 'plant.sav'
loaded_model = joblib.load(filename)
while True:
        file=open('record.txt',"r")
        a=file.read()
        file.close()
        a=[str(x) for x in a.split(" ")]
        print(a)
        j1=int(a[1])
        j2=int(a[2])
        j3=int(a[3])
        test_vals=np.array([[ 8.9,   j2,   5, 10.7, 31,   7,   j3, 1016,   1011,   j1,   4.4]])
        pred=loaded_model.predict(test_vals)
        #print(np.around(loaded_model.predict(test_vals)))
        if(pred>0.43):
                pred=1
                
        else:
                pred=0
        print(pred)
        time.sleep(14)
