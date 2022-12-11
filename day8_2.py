trees = []

with open('day8_input.txt') as f:
	for line in f:
		trees.append( list(map(int, list(line.strip()))) )

def calc_trees(input_i, input_j):
	visible_trees = [0]*4
	# left
	for i in range(input_i-1, -1, -1):
		visible_trees[0] += 1
		if trees[input_j][i] >= trees[input_j][input_i]:
			break

	# up
	for j in range(input_j-1, -1, -1):
		visible_trees[1] += 1
		if trees[j][input_i] >= trees[input_j][input_i]:
			break

	# right
	for i in range(input_i+1, len(trees[0])):
		visible_trees[2] += 1
		if trees[input_j][i] >= trees[input_j][input_i]:
			break

	# down
	for j in range(input_j+1, len(trees)):
		visible_trees[3] += 1
		if trees[j][input_i] >= trees[input_j][input_i]:
			break

	return visible_trees[0]*visible_trees[1]*visible_trees[2]*visible_trees[3]

result = float('-inf')

for j in range(1, len(trees)-1):
	for i in range(1, len(trees[0])-1):
		#print(trees[j][i])
		result = max(result, calc_trees(j, i))

print(result)