# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)
bank= pd.DataFrame(bank_data)

#Code starts here
categorial_var= bank.select_dtypes(include='object')

numerical_var=bank.select_dtypes(include='number')


banks=bank.drop(columns='Loan_ID')
shape=banks.shape
print(shape)
null= banks.isnull().sum()
print(null)
bank_mode= banks.mode().iloc[0]
banks.fillna(bank_mode, inplace=True)
null_1=banks.isnull().sum().values.sum()
print(null_1)

avg_loan_amount= pd.pivot_table(banks,index=['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)
print(avg_loan_amount)


loan_approved_se=banks[(banks['Self_Employed']=='Yes') & (banks['Loan_Status']=='Y')].shape[0]
percentage_se= (loan_approved_se*100/614)
print(percentage_se)
loan_approved_nse=banks[(banks['Self_Employed']=='No') & (banks['Loan_Status']=='Y')].shape[0]
percentage_nse=(loan_approved_nse*100/614)
print(percentage_nse)

loan_term=banks['Loan_Amount_Term'].apply(lambda x : int(x) / 12)

big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)


loan_groupby= banks.groupby(by='Loan_Status')
print(loan_groupby)
loan_groupby=loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.agg([np.mean])
print(mean_values)


