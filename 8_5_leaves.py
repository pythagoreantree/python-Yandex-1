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


def print_leaves(memstruct, root):
    memory = memstruct[0]
    if memory[root][1] == -1 and memory[root][2] == -1:
        print(memory[root][0])
    if memory[root][1] != -1:
        print_leaves(memstruct, memory[root][1])
    if memory[root][2] != -1:
        print_leaves(memstruct, memory[root][2])


sequence = list(map(int, input().split()))
seg_len = len(sequence) - 1
memstruct = initmemory(seg_len)
root = createandfillnode(memstruct, sequence[0])
for j in range(1, seg_len):
    add(memstruct, root, sequence[j])
print_leaves(memstruct, root)

