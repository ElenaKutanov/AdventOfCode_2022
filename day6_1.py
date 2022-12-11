data = ''
size = 4

with open('day6_input.txt') as f:
	for line in f:
		data = list(line.strip())

for end in range(size, len(data)):
	start = end - size
	if len(set(data[start:end])) < 4:
		continue
	print(end)
	break
