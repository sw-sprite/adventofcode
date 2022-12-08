forest = []

def is_visible(idx, value, arr): 
    return max(arr[:idx]) < value or max(arr[idx+1:]) < value

def scenic_score(idx, value, arr):
    left, right = list(reversed(arr[:idx])), arr[idx+1:]

    count_left = 0
    for i in left:
        count_left = count_left + 1
        if i >= value:
            break

    count_right = 0
    for i in right:
        count_right = count_right + 1
        if i >= value:
            break
    
    # print(value, left, right, count_left, count_right)
    return count_right * count_left

if __name__ == "__main__":
    # with open("sample_input.txt") as f:
    with open("input.txt") as f:
        lines = [list(map(int, x.strip())) for x in f]

    h, w = len(lines), len(lines[0])

    forest = lines

    count = 0
    max_score = 0
    # loop through 2D list, skipping first and last rows and columns
    for i in range(1, len(forest)-1):
        for j in range(1, len(forest[i])-1):
            # access element at current index
            if is_visible(j, forest[i][j], forest[i]) or is_visible(i, forest[i][j], [k[j] for k in forest]):
                count = count + 1
            row_score = scenic_score(j, forest[i][j], forest[i])
            col_score = scenic_score(i, forest[i][j], [k[j] for k in forest])
            # print(i, j, row_score, col_score)
            # if i == 3 and j == 2:
            #     print(row_score, col_score)
            #     print()
            max_score = max(max_score, row_score * col_score)
    print("part 1:", count + 2*(h+w-2))

    
    print("part 2:", max_score)
