import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = './sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	dates,highs = [],[]

	for row in reader:
		current_date = datetime.strptime(row[0],"%Y-%m-%d")
		high = int(row[1])
		highs.append(high)
		dates.append(current_date)

	fig = plt.figure(figsize = (10,6))
	plt.plot(dates,highs,c = 'red')

	plt.title('Daily high tempreatures,July 2014',fontsize = 24)
	plt.xlabel('',fontsize = 16)

	fig.autofmt_xdate()   #绘制斜的日期标签

	plt.ylabel('tempreatures(F)',fontsize = 16)
	plt.tick_params(axis = 'both',which = 'major',labelsize =26)

	plt.show()