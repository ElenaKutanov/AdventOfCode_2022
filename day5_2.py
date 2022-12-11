crates = {}
crates[1] = 'NDMQBPZ'
crates[2] = 'CLZQMDHV'
crates[3] = 'QHRDVFZG'
crates[4] = 'HGDFN'
crates[5] = 'NFQ'
crates[6] = 'DQVZFBT'
crates[7] = 'QMTZDVSH'
crates[8] = 'MGFPNQ'
crates[9] = 'BWRM'

#crates[1] = 'ZN'
#crates[2] = 'MCD'
#crates[3] = 'P'


with open('day5_input.txt') as f:
	for line in f:
		if line[0] != 'm':
			continue
		#print(crates)
		_, count, _, from_i, _, to_i = line.strip().split()
		count, from_i, to_i = int(count), int(from_i), int(to_i)
		#print(count, from_i, to_i)
		#print(crates[to_i])

		crates[to_i] +=  crates[from_i][-count:]

		#print(crates[to_i])
		crates[from_i] = crates[from_i][:-count]
		#print(crates[from_i])

result = ''
for i in range(1, 10):
	result += crates[i][-1]
print(result)

