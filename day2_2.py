win_bonus = {'X': 0, 'Y': 3, 'Z': 6}
you_choice_bonus = {'AX': 3, 'AZ': 2, 'BX': 1, 'BZ': 3, 'CX': 2, 'CZ': 1}
draw_bonus = {'A': 1, 'B': 2, 'C': 3}

result = 0

with open('day2_1_test.txt') as f:
    for line in f:
        opponent, win = line.split()

        you = you_choice_bonus.get(opponent+win, None)
        if you == None:
            you = draw_bonus.get(opponent)

        result += win_bonus[win] + you

print(result)