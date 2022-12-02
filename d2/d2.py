with open("input.txt") as f:
    lines = []
    for line in f:
        lines.append(line) 

## X - rock, Y - paper, Z - scissors
## A - rock, B - paper, C - scissors

win = {
    'X' : 'C',
    'Y' : 'A',
    'Z' : 'B'
}
lose = {
    'X' : 'B',
    'Y' : 'C',
    'Z' : 'A'   
}
tie = {
    'X' : 'A',
    'Y' : 'B',
    'Z' : 'C'
}
score = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3
}

finsl_score = 0
for i in lines:
    a, b = i.rstrip().split(' ')
    # print(a, b)

    if win[b] == a:
        finsl_score = finsl_score + score[b] + 6
    elif lose[b] == a:
        finsl_score = finsl_score + score[b]
    elif tie[b] == a:
        finsl_score = finsl_score + score[b] + 3

print(finsl_score)
