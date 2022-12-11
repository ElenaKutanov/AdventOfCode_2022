trees = []

with open('day8_input.txt') as f:
	for line in f:
		trees.append( list(map(int, list(line.strip()))) )

def visible(input_i, input_j):
	not_visible = 0
	# left
	for i in range(input_i-1, -1, -1):
		if trees[input_j][i] >= trees[input_j][input_i]:
			not_visible += 1
			break

	if not_visible < 1:
		#print('left')
		return True

	# up
	for j in range(input_j-1, -1, -1):
		if trees[j][input_i] >= trees[input_j][input_i]:
			not_visible += 1
			break

	if not_visible < 2:
		#print('up')
		return True

	# right
	for i in range(input_i+1, len(trees[0])):
		if trees[input_j][i] >= trees[input_j][input_i]:
			not_visible += 1
			break

	if not_visible < 3:
		#print('right')
		return True

	# down
	for j in range(input_j+1, len(trees)):
		if trees[j][input_i] >= trees[input_j][input_i]:
			not_visible += 1
			break

	if not_visible < 4:
		#print('down')
		return True

	return False

all_trees = len(trees)*len(trees[0])
#print(all_trees)
visible_trees = all_trees

for j in range(1, len(trees)-1):
	for i in range(1, len(trees[0])-1):
		#print(trees[j][i])
		if not visible(i, j):
			visible_trees -= 1
			#print('NOT VISIBLE')

print(visible_trees)