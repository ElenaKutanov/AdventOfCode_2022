class Node:
	def __init__(self, name, value=0, parent=None):
		self.name = name
		self.value = value
		self.parent = parent
		self.children = []

def print_node(folder, start=1):
	print('--- level:', start)
	print(folder.name, folder.value)
	if folder.parent != None:
		print(folder.parent.name)
	for child in folder.children:
		print_node(child, start+1)


filesystem = {}
tree = None
current_node = None

with open('day7_input.txt') as f:
	for line in f:
	 	data = line.strip().split()
	 	if data[0] == '$':
		 	if data[1] == 'cd':
		 		if tree == None:
		 			new_node = Node(data[2])
		 			tree = new_node
		 			current_node = tree
		 		elif data[2] == '..':
		 			current_node = current_node.parent
		 		else:
		 			new_node = Node(data[2], parent=current_node)
		 			if current_node != None:
			 			current_node.children.append(new_node)
			 			current_node = new_node
	 	else:
	 		if data[0] != 'dir':
	 			current_node.children.append(Node(data[1], int(data[0]), tree))
	 	#print_node(tree)
	 	#print('----------------------')


def folder_size(folder):
	#print('start with folder:', folder.name)
	if len(folder.children) == 0:
		return folder.value

	size = 0
	for child in folder.children:
		child.value = folder_size(child)
		#print('child:', child.name, child.value)
		size += child.value

	folder.value = size

	#print('folder:', folder.name, folder.value)

	return size

space_used = folder_size(tree)
print('space_used:', space_used)

#print_node(tree)


def count(folder, result=0, bound=100000):
	#print('folder:', folder.name, 'result before:', result)
	if len(folder.children) == 0:
		return result

	if folder.value <= bound:
		result += folder.value

	for child in folder.children:
		result = count(child, result)
		#print('child:', child.name, 'result after:', result)

	#print('folder:', folder.name, 'result after:', result)
	return result


print('count:', count(tree))





