if __name__ == "__main__":
    # with open("sample_input.txt") as f:
    with open("input.txt") as f:
        lines = f.readline()

    print(lines)
    # for x in range(4, len(lines)):
    #     if len(set(lines[x - 4:x])) == 4:
    #         print(x)
    #         exit()
    # print(lines)

    for x in range(14, len(lines)):
        if len(set(lines[x - 14:x])) == 14:
            print(x)
            exit()