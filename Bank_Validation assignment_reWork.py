import pandas as pd

df=pd.read_excel(r"E:\Aroha Tech\Pandas Session\16th Aug\Bank_Validation_dup.xlsx")
print(df)

Target_Account={'BankID':[],'Account_type':[],'Account_no':[]}

Bank_error_records={'Seq_no':[],'Record':[],'Reason':[]}

prev=0
for (row,column) in df.iterrows():
   
    
    if type(column[1])== str :
        if len(column[1])>=7 and len(column[1])<=11:
            if column[1][1:].isdigit() :
                
                if  column[1][1:] not in Target_Account['Account_no']:
                    Target_Account['BankID'].append(column[0])
                    Target_Account['Account_type'].append(column[1][0])
                
                    Target_Account['Account_no'].append(column[1][1:])
                else:
                    Bank_error_records['Seq_no'].append(row+1)
                    Bank_error_records['Record'].append(column[1])
                    Bank_error_records['Reason'].append('Account no Should Not be duplicate')
                
               
                
            else:
                Bank_error_records['Seq_no'].append(row+1)
                Bank_error_records['Record'].append(column[1])
                Bank_error_records['Reason'].append('Account no contain string')
        else:
            Bank_error_records['Seq_no'].append(row+1)
            Bank_error_records['Record'].append(column[1])
            Bank_error_records['Reason'].append('Account no not in range 7,11 ')
    else:
        Bank_error_records['Seq_no'].append(row+1)
        Bank_error_records['Record'].append(column[1])
        Bank_error_records['Reason'].append("It Doesn't contain any Account Type")

#print("Target Account :",Target_Account)
#print('------------------------------------------------\n\n')
#print("Bank_error_records :",Bank_error_records)

ta=pd.DataFrame(Target_Account)
ber=pd.DataFrame(Bank_error_records)

print('\nTarget Table is :\n\n',ta)
print('\nBank error record is :\n\n',ber)