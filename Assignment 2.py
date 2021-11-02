'''
print Avg of wind speed
'''

def Avg_wind_speed():
    count=0
    sum_wind=0
    for i in wind_speed:
        sum_wind += i
        count += 1
    return sum_wind/count
wind_speed=[40,50,56,72,34,63,80,39]
print(Avg_wind_speed())

print(lambda a,b:a+b, 10+20)