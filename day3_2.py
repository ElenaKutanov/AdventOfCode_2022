result = 0
backs = []

with open('day3_1.txt') as f:
	for line in f:
		if len(backs) < 3:
			backs.append( set(line.strip()) )
			#print(backs)
		if len(backs) == 3:
			#print(backs)
			appears = backs[0].intersection(backs[1])
			appears = appears.intersection(backs[2])
			for a in appears:
				code = ord(a)
				if code > 96:
					result += code - 96
				else:
					result += code - 38
			backs = []
			#print(result)

print(result)