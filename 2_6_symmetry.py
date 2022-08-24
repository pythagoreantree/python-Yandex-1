def is_polyndrom(lst):
    is_pol = True
    i = 0
    j = len(lst)-1
    while i != j and i < j:
        # print(lst[i], lst[j], is_pol)
        if lst[i] != lst[j]:
            is_pol = False
            break
        i += 1
        j -= 1
    return is_pol


n = int(input())
sequence = list(map(int, input().split()))
# print(is_polyndrom(sequence))

if is_polyndrom(sequence):
    print(0)
else:
    i1 = 0
    j1 = len(sequence)-1
    polyndrome_found = False
    while i1 != j1 and not polyndrome_found:
        if sequence[i1] == sequence[j1]:
            polyndrome_found = is_polyndrom(sequence[i1:])
        i1 += 1

    symbs = []
    if polyndrome_found:
        for k in range(i1-2, -1, -1):
            symbs.append(sequence[k])
    else:
        strt = j1 - 1
        if sequence[j1] == sequence[j1 - 1]:
            strt = j1 - 2
        for k in range(strt, -1, -1):
            symbs.append(sequence[k])

    print(len(symbs))
    # print(' '.join([str(item) for item in symbs]))
    print(*symbs)

