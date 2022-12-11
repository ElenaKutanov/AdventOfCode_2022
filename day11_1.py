class Monkey:
  def __init__(self, monkey_id, items, operation, divisible, true, false):
    self.id = monkey_id
    self.items = items
    self.operation = operation
    self.divisible = divisible
    self.true = true
    self.false = false
    self.inspected = 0

  def get_level(self, old):
    #print('=', eval(self.operation))
    return eval(self.operation)

def get_monkeys():
  monkeys = []
  monkey_id, items, operation, divisible, true, false = [None]*6
  with open('day11_input.txt') as f:
    for line in f:
      data = line.strip().replace(',', '').split()

      if len(data) == 0:
        continue

      #print(data)
      if data[0].startswith('M'):
        monkey_id = int(data[1][:-1])
      elif data[1].startswith('items'):
        items = []
        for i in range(2, len(data)):
          items.append(int(data[i]))
      elif data[0].startswith('Operation'):
        operation = ''.join(data[3:])
      elif data[0].startswith('Test'):
        divisible = int(data[-1])
      elif data[1].startswith('true'):
        true = int(data[-1])
      elif data[1].startswith('false'):
        false = int(data[-1])
        m = Monkey(monkey_id, items, operation, divisible, true, false)
        monkeys.append(m)

  return monkeys

def step(monkeys, m):
  item = monkeys[m].items.pop(0)
  #print(f'item: {item}')
  level = monkeys[m].get_level(item)
  #print(f'level: {level}')
  #level //= 3
  #print(f'level//3: {level}')
  if level%monkeys[m].divisible == 0:
    monkeys[monkeys[m].true].items.append(level)
    #print(f'to monkey: {monkeys[m].true}')
  else:
    monkeys[monkeys[m].false].items.append(level)
    #print(f'to monkey: {monkeys[m].false}')

  return monkeys


def process(monkeys, times):
  worry = 0
  t = 0
  while t < times:
    print(f'round: {t}')
    for m in range(len(monkeys)):
      for i in range(len(monkeys[m].items)):
        monkeys[m].inspected += 1
        monkeys = step(monkeys, m)
    for monkey in monkeys:
      print(monkey.items)
    t += 1
  return monkeys

def monkey_business(monkeys):
  inspected = []
  for monkey in monkeys:
    inspected.append(monkey.inspected)
  inspected.sort()
  print(f'inspected: {inspected}')

  return inspected[-2]*inspected[-1]



if __name__ == '__main__':
    monkeys = get_monkeys()
    monkeys = process(monkeys, 10000)
    print(monkey_business(monkeys))

