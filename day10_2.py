def get_commands():
	commands = []

	with open('day10_input.txt') as f:
		for line in f:
			data = line.strip().split(' ')
			if len(data) == 2:
				data[1] = int(data[1])
			commands.append(data)
	return commands

class CRT:
	def __init__(self, wide, high):
		self.wide = wide
		self.high = high
		self.matrix = []
		for i in range(high):
			self.matrix.append(['-']*wide)

		self.cycle = 0
		self.X = 1
		self.position = 0

	def y(self):
		return self.cycle//self.wide

	def x(self):
		return self.cycle%self.wide

	def draw(self):
		print(f'X: {self.X}, y: {self.y()}, x: {self.x()}')
		if self.x() in [self.X-1, self.X, self.X+1]:
			self.matrix[self.y()][self.x()] = '#'
		else:
			self.matrix[self.y()][self.x()] = '.'

	def step(self):
		self.cycle += 1

	def print_matrix(self):
		for i in range(len(self.matrix)):
			print(''.join(self.matrix[i]))


def process(commands, wide, high):
	crt = CRT(wide, high)

	for cmd in commands:
		print(f'cycle: {crt.cycle}, cmd: {cmd}')
		crt.draw()
		crt.step()
		if cmd[0] == 'addx':
			crt.draw()
			crt.step()
			crt.X += cmd[1]

	crt.print_matrix()


if __name__ == '__main__':
	commands = get_commands()
	process(commands, 40, 6)




