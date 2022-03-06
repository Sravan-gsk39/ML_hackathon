import pandas as pd
import random as rd
import math
d = []
'''
we  have assumed another collection of all the visiting places in an imaginary city
with the following columns

placeID  |  placeName  | xCoordinate  |  yCoordinate
         |             |              |    
         |             |              |               
         |             |              |                              
         
'''
for i in range(1000):
    placeID =rd.randint(1,10)
    xcoordinate = rd.randint(0,10000)
    ycoordinate = rd.randint(0,10000)
    price_per_person = rd.randint(1,10)  # in hundreds
    '''
    ------------transport services -----------
    
    1  -> car
    2  -> bus
    3  ->metro
    4  ->train
    5  ->bus + metro
    6  ->biycle
    7  ->auto
    8  ->rapido
    9  ->walk + bus 
    10 ->bike
    
    '''
    transportation_services = rd.randint(1,10)
    popularity =rd.randint(1,10)        # scale based on rating    
    enjoyment = rd.randint(0,10)
    age = rd.randint(15,85)
    gender =rd.randint(0,1)
    ''' 
    ---------companions----------
    0 -> boy of age (1-12yrs)
    1 -> girls of age(1-12yrs)
    2 -> boy of age (13-19yrs)
    3 -> girls of age(13-19yrs)
    4 -> men of age(20-40yrs)
    5 -> women of age(20-40yrs)
    6 -> men of age (41-60yrs)
    7 -> women of age(41-60yrs)
    8 -> men of age(61+)
    9 -> women of age (61+)
    '''
    companion = rd.randint(0,9)
    timing_start = rd.randint(0,18)
    timing_end = timing_start + rd.randint(1,5)
    social_media_presence = rd.randint(0, 10)
    w=[5,2,5,3,0.65,30,5,2,1.5,3]
    num_of_features = 13
    out = math.ceil((price_per_person *w[0]+transportation_services *w[1]+popularity *w[2]+enjoyment *w[3]+age *w[4]+gender *w[5]+companion *w[6]+timing_start *w[7]+timing_end *w[8]+social_media_presence *w[9])/num_of_features)
    threshold = 22
    if out>threshold:
        clss = 1
    else:
        clss = 0
    d.append([placeID,xcoordinate,ycoordinate,price_per_person,transportation_services,popularity,enjoyment,age,gender,companion,timing_start,timing_end,social_media_presence,out,clss])
df = pd.DataFrame(d,columns=['placeID','xcoordinate','ycoordinate','price_per_person','transportation_services','popularity','enjoyment','age','gender','companion','timing_start','timing_end','social_media_presence','out','clss'])
df.to_csv('data.csv',index=False)