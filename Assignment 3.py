'''
what dates the events rain
'''

def rain_event():
    rain_list_date=[]
    for i in date.keys():
        #print(i)
        if date[i]=='rain':
            #print(i)
            rain_list_date.append(i)
    return rain_list_date
        
    
date={'01-09-2016':'rain','01-01-2016':'NaN','01-10-2016':'rain','1/16/2016':'rain','1/17/2016':'Fog-Snow'}
print(rain_event())
