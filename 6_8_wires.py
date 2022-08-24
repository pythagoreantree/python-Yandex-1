def rbinsearch(l, r, check, params):
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid, params):
            l = mid
        else:
            r = mid - 1
    return l


def check_length(x, params):
    segnum, segs = params
    seg_counter = 0
    for seg in segs:
        seg_counter += seg // x
    # print(x, seg_counter, segnum)
    return seg_counter >= segnum


n, k = map(int, input().split())
wires = []
for _ in range(n):
    wire = int(input())
    wires.append(wire)

min_l = wires[0]
for w in wires:
    min_l = max(w, min_l)

# print(min_l)
ans = rbinsearch(0, min_l, check_length, (k, wires))
print(ans)
