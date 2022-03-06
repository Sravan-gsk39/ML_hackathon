# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 03:27:36 2022

@author: jashwanth
"""

import pandas as pd
from sklearn.svm import SVC # "Support Vector Classifier"
points=["charminar","museum","amusement park ","sports arena","mall","golconda fort","beach","snow world","cafe","zoo"]
def get_possible_place(file,impacts,outcome,inps):
    data = pd.read_csv(file)
    X = data[impacts]
    Y = data[outcome]
    Y=Y.round()
    clf = SVC(kernel='linear') 
    clf.fit(X,Y)
    nx = [inps]
    pred = clf.predict(nx)
    return pred


xcoordinate=int(input("xcoordinate : "))
ycoordinate=int(input("ycoordinate : "))
price_per_person = int(input("enter budget : "))
transportation_services = int(input("enter transportation services"))
popularity =int(input("enter popularity scale"))   
enjoyment = int(input("enjoyment :"))
age = int (input("age : "))
gender =int(input("gender : "))
companion = int(input("comparision : "))
timing_start=int(input("start_time : "))
timing_end=int(input("end time : "))
social_media_presence = int(input("enter social media presence : "))
print("-------------------------------------------------------------------------------")
for i in range(1,10):    
    p = get_possible_place('data.csv',['placeID','xcoordinate','ycoordinate','price_per_person','transportation_services','popularity','enjoyment','age','gender','companion','timing_start','timing_end','social_media_presence'],"clss",[i,xcoordinate,ycoordinate,price_per_person,transportation_services,popularity,enjoyment,age,gender,companion,timing_start,timing_end,social_media_presence])
    if(p[0]==0):
        print("check out place ",points[i]," you may like it")



