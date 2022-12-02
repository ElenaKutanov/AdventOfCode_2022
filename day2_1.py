scores = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
win_bonus = {'AY': 6, 'BX': 0, 'BZ': 6, 'CY': 0, 'CX': 6, 'AZ': 0}

result = 0

with open('day2_1.txt') as f:
    for line in f:
        opponent, you = line.split()
        result += scores[you] + win_bonus.get(opponent+you, 3)

print(result)