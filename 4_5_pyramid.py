n = int(input())
# 3 1
# 2 2
# 3 3

blocks = {}
for _ in range(n):
    w, h = map(int, input().split())
    if w not in blocks:
        list = [h]
        blocks[w] = list
    blocks[w].append(h)

res_h = 0
for key in sorted(blocks.keys(), reverse=True):
    res_h += sorted(blocks[key], reverse=True)[0]

print(res_h)






