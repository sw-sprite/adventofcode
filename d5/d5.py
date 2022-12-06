def parse_stacks(stack_txt):
    stack_txt_list = stack_txt.split("\n")
    # for i in range(len(stack_txt_list) - 1):
    #     stack_txt_list[i] = stack_txt_list[i].strip().split(" ")
    
    print(stack_txt_list)
    # print(stack_txt_list[-1].strip().split("   "))
    stacks = [[] for i in range(len(stack_txt_list[-1].split("   ")))]
    # print(stacks)
    # for i in stacks:



# Driver Code
# cheating since parsing input into stacks is a pain, might
# come back later to write a proper parser 
if __name__ == "__main__":

    # with open("sample_input.txt") as f:
    with open("input_without_stack.txt") as f:
    # with open("sample_input_without_stack.txt") as f:
        lines = f.read().split('\n')

    stacks = [[
        'D', 'H', 'R', 'Z', 'S', 'P', 'W', 'Q'
    ], [
        'F', 'H', 'Q', 'W', 'R', 'B', 'V'
    ], [
        'H', 'S', 'V', 'C'
    ], [
        'G', 'F', 'H'
    ], [
        'Z', 'B', 'J', 'G', 'P'
    ], [
        'L', 'F', 'W', 'H', 'J', 'T', 'Q'
    ], [
        'N', 'J', 'V', 'L', 'D', 'W', 'T', 'Z'
    ], [
        'F', 'H', 'G', 'J', 'C', 'Z', 'T', 'D'
    ], [
        'H', 'B', 'M', 'V', 'P', 'W'
    ]]

    sample_stacks = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

    # for i in lines:
    #     instructions = i.strip().split(' ')
    #     print(instructions, int(instructions[3])-1, int(instructions[5])-1)
    #     for j in range(int(instructions[1])):
    #         temp = sample_stacks[int(instructions[3])-1].pop(0)
    #         sample_stacks[int(instructions[5])-1].insert(0, temp)

    # for i in sample_stacks:
    #     print(i[0])
    # print(sample_stacks)
    for i in lines:
        instructions = i.strip().split(' ')
        print(instructions, int(instructions[3])-1, int(instructions[5])-1)
        for j in range(int(instructions[1])):
            temp = stacks[int(instructions[3])-1].pop(0)
            stacks[int(instructions[5])-1].insert(0, temp)

    for i in stacks:
        print(i[0], end="")
    print(stacks)