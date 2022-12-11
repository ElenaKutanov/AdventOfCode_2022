import operator

ops = {'+': operator.add, '*': operator.mul}

class Item:
  def __init__(self, monkey_id, item):
    self.monkey_id = monkey_id
    self.item = item
    self.operations = []
    self.numbers = []

class Monkey:
  def __init__(self, monkey_id, items, operation, divisible, true, false):
    self.id = monkey_id
    self.items = items
    self.operation = operation
    self.divisible = divisible
    self.true = true
    self.false = false
    self.inspected = 0
  
  def print_monkey(self):
    print(f'Monkey: {self.id}')
    print(f'Operation: {self.operation}')


  # def get_level(self, old):
  #   #print('=', eval(self.operation))
  #   return eval(self.operation)

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
          item = Item(monkey_id, int(data[i]))
          items.append(item)
      elif data[0].startswith('Operation'):
        operation = data[3:]
      elif data[0].startswith('Test'):
        divisible = int(data[-1])
      elif data[1].startswith('true'):
        true = int(data[-1])
      elif data[1].startswith('false'):
        false = int(data[-1])
        m = Monkey(monkey_id, items, operation, divisible, true, false)
        monkeys.append(m)

  return monkeys

def update_operations(item, operation):
  if len(item.operations) > 0 and item.operations[-1] == '+':
     item.numbers[-1] += int(operation[2])
  elif operation[2] == 'old':
    # TODO
    pass
  else:
      item.operations.append(operation[1])
      item.numbers.append(int(operation[2]))
  
  return item

def level_divisible(item, divisible):
  result = item.item % divisible
  print(f'item.numbers: {item.numbers}')
  for i, operation in enumerate(item.operations):
    result = ops[operation](result, item.numbers[i]%divisible)
  
  if result%divisible:
    return True
  
  return False

def step(monkeys, m):
  item = monkeys[m].items.pop(0)
  #print(f'item: {item}')
  #level = monkeys[m].get_level(item)
  item = update_operations(item, monkeys[m].operation)

  if level_divisible(item, monkeys[m].divisible):
  #print(f'level: {level}')
  #level //= 3
  #print(f'level//3: {level}')
  #if level%monkeys[m].divisible == 0:
    monkeys[monkeys[m].true].items.append(item)
    #print(f'to monkey: {monkeys[m].true}')
  else:
    monkeys[monkeys[m].false].items.append(item)
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
    monkeys = process(monkeys, 20)
    print(monkey_business(monkeys))

