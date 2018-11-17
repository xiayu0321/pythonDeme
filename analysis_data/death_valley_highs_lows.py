import csv
from matplotlib import pyplot as plt 
from datetime import datetime

dates,highs,lows = [],[],[]
filename = './death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	header = next(reader)

	for row in reader:
		try:
			current_date = datetime.strptime(row[0],'%Y-%m-%d')
			high = int(row[1])
			low = int(row[2])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

	fig = plt.figure(figsize = (10,6))
	plt.plot(dates,highs,c = 'red',alpha = 0.5)
	plt.plot(dates,lows,c = 'blue',alpha = 0.5)
	plt.fill_between(dates,highs,lows,facecolor = 'blue',alpha = 0.1)

	plt.title("high and low tempreture in 2014",fontsize = 24)
	plt.xlabel('',fontsize = 14)
	plt.ylabel('tempreatures(F)',fontsize = 14)
	plt.tick_params(axis = 'both',which = 'major',labelsize = 24)

	fig.autofmt_xdate()

	plt.show()



