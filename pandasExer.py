import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.mpl_style','default')
plt.rcParams['figure.figsize'] = (15,6)

broken_df = pd.read_csv('bikes.csv',sep=';',encoding = 'latinl',parse_dates=['Date'],dayfirst = True)
print(broken_df[:3])
