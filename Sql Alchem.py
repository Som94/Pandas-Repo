'''
sqlalchemy is use for to convert pandas dataFrame to sql table.

'''


import pandas as pd
import sqlalchemy

name='root'            # Your MySQL User name
password='root'        # Your Password
database_name='test'   # your Database Name

#Create a Engine 
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

#Execute sql query through the engine
df = pd.read_sql_query("select * from emp;", engine)
#print Executed data 
print(df)

# To create a table with the existing dataFrame in the  MySQL Database.
# If given table already exists in mysql db then it will be append with that data.
# Otherwise it Create a new table.
# This table  doesn't contain any constraints, 
# If You want add any Constraints, then after creation of table you can add
  
df.to_sql(name='temp',con=engine,if_exists='append',index=False)

# To Read a CSV File
dft=pd.read_csv(r'E:\Aroha Tech\AWS Session\vehicle_income_expense_master.csv')
print(dft)


dft.to_sql(name='viem',con=engine,if_exists='append',index=False)

dftt=pd.read_csv(r'E:\Aroha Tech\AWS Session\s3 Bucket\15th Aug\vehicle_master.csv',header=None, names=['ID_VEHICLE','REG_NUMBER','NICK_NAME','ID_BRANCH','VEHICLE_TYPE','MAKER','MODEL','PRODUCT_TYPE'])
print(dftt)

dftt.to_sql(name='vehicle_master_duplicate',con=engine,if_exists='append',index=False)