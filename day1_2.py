bag = []

with open('day1_1.txt') as f:
	temp = 0
	for line in f:
		if line == '\n':
			bag.append(temp)
			temp = 0
		else:
			temp += int(line)

bag.sort()
print( sum(bag[-3:]) )

print( bag[-3:] )