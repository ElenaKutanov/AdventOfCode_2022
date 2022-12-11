data = []
size = float('-inf')

with open('day9_input.txt') as f:
	for line in f:
		direction, count = line.strip().split()
		size = max(size, int(count))
		data.append([direction, int(count)])

road = []
for _ in range(size):
	road.append(['.']*size)

H, T = [0,0], [0,0]

steps = set()
steps.add(tuple(T))

def print_matrix(steps):
	result = []
	for _ in range(20):
		result.append(['.']*30)

	for step in steps:
		result[step[1]+8][step[0]+15] = '#'

	for line in result:
		print(line)

	print('\n')

def move_horizontal(H, T, save):
	#print('move_horizontal')
	#print(direction)
	if H[0] > T[0]:
		#print('Range', range(T[0], H[0]))
		T[0] += 1
	else:
		T[0] -= 1

	if save: steps.add(tuple(T))

	return T

def move_vertical(H, T, save):
	#print(direction)
	if H[1] > T[1]:
		T[1] += 1 
	else:
		T[1] -= 1

	if save: steps.add(tuple(T))

	return T

def move_diagonal(H, T, save):
	if H[0] > T[0]:
		T[0] += 1
	else:
		T[0] -= 1

	if H[1] > T[1]:
		T[1] += 1
	else:
		T[1] -= 1

	if save:
		steps.add(tuple(T))

	return T


def move_T(H, T, direction, save=False):
	x_diff = abs(H[0]-T[0])
	y_diff = abs(H[1]-T[1])
	#if save:
		#print(f'H: {H}')
		#print(f'T: {T}')
		#print(f'Initial x_diff {x_diff}, y_diff {y_diff}')

	while x_diff > 1 or y_diff > 1:
		#print('while')
		if not y_diff:
			#print('move_horizontal')
			T = move_horizontal(H, T, save)
		elif not x_diff:
			#print('move_vertical')
			T = move_vertical(H, T, save)
		else:
			#print('move_diagonal')
			T = move_diagonal(H, T, save)

		x_diff = abs(H[0]-T[0])
		y_diff = abs(H[1]-T[1])
		#print(f'Corrected x_diff {x_diff}, y_diff {y_diff}')
		#print(f'Corrected T: {T}')
		#print('Temp len steps:', len(steps))
		#print('Temp steps:', steps)
		#if save:
			#print(f'Corrected x_diff {x_diff}, y_diff {y_diff}')
			#print(f'Corrected T: {T}')
			#print_matrix(steps)

	return T

tails = []
for _ in range(9):
	tails.append([0,0])

def update_tails(H):
	#print('H:', H)
	for t, tail in enumerate(tails):
		#print(t)
		save = False
		if t == 8:
			save = True
		if t == 0:
			tails[t] = move_T(H, tails[t], direction)
		else:
			tails[t] = move_T(tails[t-1], tails[t], direction, save)
	#print('tails:', tails)


for direction, count in data:
	#print(f'direction {direction}, count {count}')
	#new_H = update_H(H, direction, count)

	for _ in range(count):
		if direction == 'R':
			H[0] += 1
		elif direction == 'L':
			H[0] -= 1
		elif direction == 'D':
			H[1] += 1
		elif direction == 'U':
			H[1] -= 1
		update_tails(H)



#print(steps)
print(len(steps))




