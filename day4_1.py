result = 0

def get_range(elf):
	start, end = list(map(int, elf.split('-')))
	return set(range(start, end+1))

with open('day4_input.txt') as f:
	for line in f:

		elf1, elf2 = line.strip().split(',')
		#print(elf1,elf2)
		range1, range2 = get_range(elf1), get_range(elf2)
		#print(range1, range2)
		overlap = range1.intersection(range2)
		#print(overlap)

		if overlap in [range1, range2]:
			result += 1

print(result)
