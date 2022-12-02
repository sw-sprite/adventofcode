with open("input.txt") as f:
    lines = []
    for line in f:
        lines.append(line) 

## X - lose, Y - draw, Z - win
## A - rock, B - paper, C - scissors

win = {
    'A' : 'B',
    'B' : 'C',
    'C' : 'A'
}
lose = {
    'A' : 'C',
    'B' : 'A',
    'C' : 'B'   
}
tie = {
    'A' : 'A',
    'B' : 'B',
    'C' : 'C'
}

score = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}

finsl_score = 0
for i in lines:
    a, b = i.rstrip().split(' ')
    # print(a, b)

    if b == "Y":
        finsl_score = finsl_score + score[tie[a]] + 3
    elif b == "X":
        finsl_score = finsl_score + score[lose[a]]
    elif b == "Z":
        finsl_score = finsl_score + score[win[a]] + 6

print(finsl_score)
