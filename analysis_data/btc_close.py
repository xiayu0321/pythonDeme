import json
import pygal
import math

filename = './btc_close_2017_urllib.json'

with open(filename) as f:
	btc_data = json.load(f)

dates,months,weeks,weekdays,closes = [],[],[],[],[]
for btc_dict in btc_data:
	date = btc_dict['date']
	month = int(btc_dict['month'])
	week = int(btc_dict['week'])
	weekday = btc_dict['weekday']
	close =int(float(btc_dict['close'])) 

	dates.append(date)
	months.append(month)
	weeks.append(week)
	weekdays.append(weekday)
	closes.append(close)

line_chart = pygal.Line(x_label_rotation = 20,show_minor_x_labels = False)
line_chart.title = '收盘价'
line_chart.x_labels = dates
N =20
line_chart.x_labels_major = dates[::N]
closes_log = [math.log10(_) for _ in closes]
#line_chart.add('收盘价',closes)
#line_chart.render_to_file('收盘价折线图.svg')

line_chart.add('log收盘价',closes_log)
line_chart.render_to_file('收盘价对数变换折线图.svg')


