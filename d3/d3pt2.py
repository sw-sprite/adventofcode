## a = ord('a') - 96
## A = ord('A')- 38

def return_dup(arr_input):
    arr_input = map(lambda s: s.strip(), arr_input)
    x = list(set.intersection(*map(set,arr_input)))
    print(x)
    return x[0]

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
    
    elf_groups = [lines[x:x+3] for x in range(0, len(lines), 3)]
    sum = 0
    for i in elf_groups:
        rep_char = return_dup(i)
        cur_step_score = return_score(rep_char)
        
        print(i, rep_char, cur_step_score)
        # print(rep_char, cur_step_score)
        sum = sum + cur_step_score
    print(sum)