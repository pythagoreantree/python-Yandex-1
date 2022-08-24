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
    if x == key:
        return 0
    elif x < key:
        left = memory[root][1]
        if left == -1:
            memory[root][1] = createandfillnode(memstruct, x)
            return 1
        else:
            h = add(memstruct, left, x)
            h += 1
    elif x > key:
        right = memory[root][2]
        if right == -1:
            memory[root][2] = createandfillnode(memstruct, x)
            return 1
        else:
            h = add(memstruct, right, x)
            h += 1
    return h


sequence = list(map(int, input().split()))

# print(sequence)

seg_len = len(sequence) - 1
memstruct = initmemory(seg_len)
root = createandfillnode(memstruct, sequence[0])

max_h = 0
for j in range(1, seg_len):
    tree_height = add(memstruct, root, sequence[j])
    if tree_height > max_h:
        max_h = tree_height

print(max_h + 1)

