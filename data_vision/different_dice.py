import pygal

from die import Die

die_1 = Die()
die_2 = Die(10)

results = []

for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

friquencies = []

max_result = die_1.num_sides + die_2.num_sides

for value in range(11,max_result+1):
	friquency = results.count(value)
	friquencies.append(friquency)


hist = pygal.Bar()
hist.title = "Results of rolliing a D6 and a D10 1000 times"
hist.x_label = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add('D6 + D10',friquencies)
hist.render_to_file('different_dice.svg')