import pandas as pd
import numpy as np
from collections import Counter
from sklearn import preprocessing
from matplotlib import pyplot as plt
#%matplotlib inline
import seaborn as sns
import xlrd
import missingno

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
sns.set(font = 'SimHei')

data = pd.read_excel('dummy.xlsx')
print(data)
print("data.head----------------------")
print(data.head())
print("data.shape----------------------")
print(data.shape)
print("data.describe----------------------")
print(data.describe())
print("data.isnull().any()----------------------")
print(data.isnull().any())
print("total----------------------")
total = data.isnull().sum().sort_values(ascending = False)
print(total)
print("percent----------------------")
percent = (data.isnull().sum()/data.isnull().count()).sort_values(ascending = False)
missing_data = pd.concat([total,percent],axis = 1,keys = ['Total','Percent'])
print(missing_data.head(20))
print("missingno----------------")
missingno.matrix(data)
#data = data.dropna(thresh=data.shape[0]*0.5,axis = 1)
#data.dropna(axis = 0,how = 'all')
print(data.fillna(0))
print("统计重复记录数-----------")
print(data.duplicated().sum())
data.drop_duplicates()
print("分离连续与离散-----------")
data.columns

id_col=['姓名']
cat_col = ['学历','学校']
cont_col=['成绩','能力']

print (data[cat_col])
print (data[cont_col])

print("计算出现的频次----------")
for i in cat_col:
    print(pd.Series(data[i]).value_counts())
