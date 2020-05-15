# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file

data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
shape=np.shape(data)

census=np.concatenate([new_record,data],axis=0)

shape_1=np.shape(census)
print(shape_1)
age=census[:,0]
print(age)
max_age=np.max(age)
print(max_age)
min_age= np.min(age)
print(min_age)
age_mean=np.mean(age)
print(age_mean)
age_std= np.std(age)
print(age_std)
print('=========')

race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0= len(race_0)
len_1= len(race_1)
len_2= len(race_2)
len_3= len(race_3)
len_4= len(race_4)
race=np.array([len_0,len_1,len_2,len_3,len_4])
print(race)
minority_race= np.argmin(race)
print(minority_race)

senior_citizens=census[census[:,0]>60]


working_hours_sum=senior_citizens.sum(axis=0)[6]
print(working_hours_sum)
senior_citizens_len= len(senior_citizens)
print(senior_citizens_len)
avg_working_hours= (working_hours_sum)/(senior_citizens_len)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high= high.mean(axis=0)[7]
print(avg_pay_high)
avg_pay_low= low.mean(axis=0)[7]
print(avg_pay_low)
compare=avg_pay_high-avg_pay_low
print(compare)


