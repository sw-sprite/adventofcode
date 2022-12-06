## a = ord('a') - 96
## A = ord('A')- 38

def return_dup(str_input):
    ceiliing_div = len(str_input)//2
    a, b = str_input[:ceiliing_div], str_input[ceiliing_div:]
    
    print(a, b)
    for i in a:
        if i in b:
            return i
    return 0

def return_score(char_input):
    if ord(char_input) >= 97:
        return ord(char_input) - 96
    else: 
        return ord(char_input) - 38

# Driver Code
if __name__ == "__main__":

    # with open("sample_input.txt") as f:
    with open("input.txt") as f:
        lines = []
        for line in f:
            lines.append(line) 
    
    sum = 0
    for i in lines:
        rep_char = return_dup(i[:-1])
        cur_step_score = return_score(rep_char)
        print(rep_char, cur_step_score)
        sum = sum + cur_step_score
    print(sum)