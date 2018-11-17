import json
import pygal
import math
from itertools import groupby

def draw_line(x_data,y_data,title,y_legend):
    xy_map = []

    for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
        y_list = list(v for _,v in y)
        xy_map.append([x,sum(y_list) / len(y_list)])

    x_unique,y_mean = zip(*xy_map)

    line_chart = pygal.Line()
    line_chart.title = title

    #重点 map(str())    
    line_chart.x_labels = map(str,x_unique)
    line_chart.add(y_legend,y_mean)
    line_chart.render_to_file(title+'.svg')

    return line_chart

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

idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(months[:idx_month],closes[:idx_month],'close average price','average price')
line_chart_month

idx_week = dates.index('2017-12-11')
line_chart_week = draw_line(weeks[1:idx_week],closes[1:idx_week],'closed sunday price','sunday average price')
line_chart_week


idx_week = dates.index('2017-12-11')
print(idx_week)
wd = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
line_chart_weekend = draw_line(weekdays_int,closes[1:idx_week],'closed week price','week average price')
line_chart_weekend.x_labels = ['周一','周二','周三','周四','周五','周六','周天']
line_chart_weekend.render_to_file('week average closed price.svg')


with open('close price Dashboard.html','w',encoding = 'utf-8') as html_file:
    html_file.write('<html><head><title>close price Dashboard</title><meta charset = "utf-8"></head></body>\n')
    for svg in ['close average price.svg','closed sunday price.svg','closed week price.svg'
        ]:
            html_file.write('   <object type="image/svg+xml" data = "{0}" height = 500></object>\n'.format(svg))
            html_file.write('</body></html>')

        