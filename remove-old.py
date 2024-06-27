#!/usr/bin/env python3
from pprint import pprint as PP

with open('ldt.csv') as f:
	data = f.read()

data = data.split('\n')
data = [i.split(',') for i in data]

PP(data)

removed = []
for k, v in enumerate(data):
	try:
		name = v[1]
		parent = v[3]
		start = v[4]
		stop = v[5]
		if not stop == "":
			v[2] = "#cccccc"
			# removed.append(name)
			# data[k] = [""] * len(data[0])
		# if parent in removed:
		# 	v[3] = ""
	except IndexError:
		pass

data = '\n'.join([
	','.join(i) for i in data
	])

with open('ldt.csv', 'w') as f:
	f.write(data)

