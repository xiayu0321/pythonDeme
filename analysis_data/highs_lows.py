import csv

from matplotlib import pyplot as plt
from datetime import datetime

filename = './sitka_weather_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)

	datas,highs,lows= [],[],[]

	for row in reader:
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		datas.append(current_date)

		high = int(row[1])
		highs.append(high)

		low = int(row[3])
		lows.append(low)


	fig = plt.figure(figsize = (10,6))
	plt.plot(datas,highs,c = 'red',alpha = 0.5)
	plt.plot(datas,lows,c = 'blue',alpha = 0.5)
	plt.fill_between(datas,highs,lows,facecolor = 'blue',alpha = 0.1)

	plt.title('Daily high and low temperatures - 2014',fontsize = 24)
	plt.xlabel('',fontsize = 14)
	plt.ylabel('tempreatures(F)',fontsize = 14)
	plt.tick_params(axis = 'both',which = 'major',labelsize =26)

	fig.autofmt_xdate()
	plt.show()