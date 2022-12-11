commands = []

with open('day10_input.txt') as f:
	for line in f:
		data = line.strip().split(' ')
		if len(data) == 2:
			data[1] = int(data[1])
		commands.append(data)


strengths = []
cycle = 0
X = 1

during = [20, 60, 100, 140, 180, 220]

def check_strength():
	if cycle in during:
		strength = X*cycle
		print(X, cycle)
		print(strength)
		strengths.append(strength)

for cmd in commands:
	
	print(f'cycle: {cycle}, cmd: {cmd}')
	if cmd[0] == 'noop':
		cycle += 1
		check_strength()
	else:
		cycle += 1
		check_strength()
		cycle += 1
		check_strength()
		X += cmd[1]
	#check_strength()
	print(f'new cycle: {cycle}, X: {X}')

print(strengths)
print(sum(strengths))


