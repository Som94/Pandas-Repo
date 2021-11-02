'''
Print maximum tempreture
'''

def max_temp():
    maxt=0
    for i in tempreture:
        if i>maxt:
            maxt=i
    return maxt
tempreture=[41,30,20,40,35,112,3,98,1,46,17]
print('The Maximum is:',max_temp())

    