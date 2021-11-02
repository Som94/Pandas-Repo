import pandas as pd

df=pd.read_csv('E:\Aroha Tech\Pandas Session\Data_Outlet.csv')
print(df)

#group_by_item_fact_contain=df.groupby('Item_Fat_Content' )
#print(group_by_item_fact_contain)


#-------------Convert Low Fat as 0 and Regular as 1----------------------------

convrt=df['Item_Fat_Content']
Item_Fat_Content_dup=[]
for i in convrt:
    if i[0].upper()=='L':
        i='Low Fat'
        #print(i)
        Item_Fat_Content_dup.append(i)
    else:
        i='Regular'
        #print(i)
        Item_Fat_Content_dup.append(i)
        
#print(Item_Fat_Content_dup)

df['Item_Fat_Content']=Item_Fat_Content_dup

make_zero_one_list=[]

for j in df['Item_Fat_Content']:
    if j=='Low Fat':
        make_zero_one_list.append(0)
    else:
        make_zero_one_list.append(1)
        
#print(make_zero_one_list)

df['Item_Fat_Content']=make_zero_one_list

print(df)
#------------------- End -------------------------------

#------ Divided Outlet_Size into 3 parts as High_outlet, medium_outlet, small_outlet-------

#d=df['Outlet_Size'].fillna('Small', inplace=True)

#print(d)


groupby_outlet_type=df.groupby("Outlet_Type")

for i,j in groupby_outlet_type:
    #print(i)
    
    if i=='Grocery Store':
        get_group_outlet_type=groupby_outlet_type.get_group("Grocery Store")
        df['Outlet_Size']=get_group_outlet_type["Outlet_Size"].fillna(get_group_outlet_type["Outlet_Size"].mode()[0] , inplace=True)
        #print(get_group_outlet_type["Outlet_Size"])
    if i=='Supermarket Type1':
        get_group_outlet_type=groupby_outlet_type.get_group("Supermarket Type1")
        df['Outlet_Size']=get_group_outlet_type["Outlet_Size"].fillna(get_group_outlet_type["Outlet_Size"].mode()[0] , inplace=True)
        #print(get_group_outlet_type["Outlet_Size"])
    if i=='Supermarket Type2':
        get_group_outlet_type=groupby_outlet_type.get_group("Supermarket Type2")
        df['Outlet_Size']=get_group_outlet_type["Outlet_Size"].fillna(get_group_outlet_type["Outlet_Size"].mode()[0] , inplace=True)
        #print(get_group_outlet_type["Outlet_Size"])
    if i=='Supermarket Type3':
        get_group_outlet_type=groupby_outlet_type.get_group("Supermarket Type3")
        df['Outlet_Size']=get_group_outlet_type["Outlet_Size"].fillna(get_group_outlet_type["Outlet_Size"].mode()[0] , inplace=True)
        #print(get_group_outlet_type["Outlet_Size"])
        
        
print(df)
#--------------------------------------------------------

small_list=[]

medium_list=[]

high_list=[]

for i in df['Outlet_Size']:
    #print(type(i))
    if str(i).lower()== 'small':
        small_list.append(1)
        medium_list.append(0)
        high_list.append(0)
    if str(i).lower()=='medium':
        small_list.append(0)
        medium_list.append(1)
        high_list.append(0)
        
    if str(i).lower()=='high':
        small_list.append(0)
        medium_list.append(0)
        high_list.append(1)

df['Small_Size']=small_list
df['Medium_Size']=medium_list
df['High_Size']=high_list

df.drop('Outlet_Size', inplace=True, axis=1)

print(df)


#-------- 3.Done same to Outlet_type as Q2. like create 4 columns as Outlet_type and put values------

Grocery_Store=[]
Supermarket_Type1=[]
Supermarket_Type2=[]
Supermarket_Type3=[]


for i in df['Outlet_Type']:
    #print(type(i))
    if i=='Grocery Store':
        
        Grocery_Store.append(1)
        Supermarket_Type1.append(0)
        Supermarket_Type2.append(0)
        Supermarket_Type3.append(0)
        
    if i=='Supermarket Type1':
        
        Grocery_Store.append(0)
        Supermarket_Type1.append(1)
        Supermarket_Type2.append(0)
        Supermarket_Type3.append(0)
        
    if i=='Supermarket Type2':
        
        Grocery_Store.append(0)
        Supermarket_Type1.append(0)
        Supermarket_Type2.append(1)
        Supermarket_Type3.append(0)
        
    if i=='Supermarket Type3':
        
        Grocery_Store.append(0)
        Supermarket_Type1.append(0)
        Supermarket_Type2.append(0)
        Supermarket_Type3.append(1)
        


df['Grocery_Store']=Grocery_Store
df['Supermarket_Type1']=Supermarket_Type1
df['Supermarket_Type2']=Supermarket_Type2
df['Supermarket_Type3']=Supermarket_Type3


        




