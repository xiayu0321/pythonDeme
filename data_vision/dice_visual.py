import pygal

from die import Die

die_1 = Die()
die_2 = Die()

results = []

for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

frequencies = []

max_result = die_1.num_sides + die_2.num_sides

for value in range(2,max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

hist = pygal.Bar()

hist.title = "results of rolling two D6 dice 1000 times"
hist.x_labels = [str(x) for x in range(2,max_result+1)]
hist.x_title = "results"
hist.y_title = "frequency of results"

hist.add('D6 + D6',frequencies)
hist.render_to_file('dice_visual.svg')
