def fully_covers(l1, r1, l2, r2):
    s1 = set(range(int(l1), int(r1) + 1))
    s2 = set(range(int(l2), int(r2) + 1))
    if s1.issubset(s2) or s2.issubset(s1):
        return True
    return False

def overlaps(l1, r1, l2, r2):
    s1 = set(range(int(l1), int(r1) + 1))
    s2 = set(range(int(l2), int(r2) + 1))
    if sum(s1.intersection(s2)) > 0 or sum(s2.intersection(s1)) > 0:
        return True
    return False
   

# Driver Code
if __name__ == "__main__":
    # with open("sample_input.txt") as f:
    with open("input.txt") as f:
        lines = []
        for line in f:
            lines.append(line) 
    
    count = 0
    for i in lines:
        l, r = i.split(",")
        l1, r1 = l.strip().split(("-"))
        l2, r2 = r.strip().split(("-"))
        print(i[:-1])
        print(l1, r1, l2, r2)
        # if fully_covers(l1, r1, l2, r2):
        if overlaps(l1, r1, l2, r2):
            count = count + 1
        
    print(count)