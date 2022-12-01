max_bag = 0

with open('day1_1.txt') as f:
	temp = 0
	for line in f:
		if line == '\n':
			max_bag = max(max_bag, temp)
			temp = 0
		else:
			temp += int(line)

print(max_bag)