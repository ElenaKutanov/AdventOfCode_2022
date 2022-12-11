result = 0

with open('day3_1.txt') as f:
	for line in f:
		data = line.strip()
		bound = len(data)//2
		part1, part2 = set(data[0:bound]), set(data[bound:])
		appears = part1.intersection(part2)
		for a in appears:
			code = ord(a)
			if code > 96:
				result += code - 96
			else:
				result += code - 38
			#print(result)

print(result)