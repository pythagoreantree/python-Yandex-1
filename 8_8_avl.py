def initmemory(n):
    memory = []
    for i in range(n):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree


def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index


def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index


def add(memstruct, root, x):
    memory = memstruct[0]
    key = memory[root][0]
    if x < key:
        left = memory[root][1]
        if left == -1:
            memory[root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memory[root][2]
        if right == -1:
            memory[root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)


def traverse_tree(memstruct, root):
    memory = memstruct[0]
    if memory[root][1] == -1 and memory[root][2] == -1:
        return 1, True
    left_h, right_h = 0, 0
    is_avl_balanced_l, is_avl_balanced_r = True, True
    if memory[root][1] != -1:
        left_h, is_avl_balanced_l = traverse_tree(memstruct, memory[root][1])
    if memory[root][2] != -1:
        right_h, is_avl_balanced_r = traverse_tree(memstruct, memory[root][2])
    is_avl_balanced = is_avl_balanced_l and is_avl_balanced_r
    if abs(right_h - left_h) > 1:
        is_avl_balanced = False
    return max(left_h, right_h) + 1, is_avl_balanced


sequence = list(map(int, input().split()))
seg_len = len(sequence) - 1
memstruct = initmemory(seg_len)
root = createandfillnode(memstruct, sequence[0])
for j in range(1, seg_len):
    add(memstruct, root, sequence[j])
h, is_avl = traverse_tree(memstruct, root)
if is_avl:
    print('YES')
else:
    print('NO')


