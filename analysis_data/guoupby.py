from itertools import groupby
x_data = [1,3,2]
y_data = [4,5,6]

for x,y in groupby(sorted(zip(x_data,y_data)),key = lambda _:_[0]):
	x_list = x
	y_list = list(y)
	print(x)
	print(y_list)
