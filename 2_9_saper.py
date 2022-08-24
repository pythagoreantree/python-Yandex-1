n, m, k = map(int, input().split())
bbs = []
for _ in range(0, k):
    p, q = map(int, input().split())
    bbs.append([p, q])

mtrx = [[0 for x in range(m+2)] for y in range(n+2)]
# print(mtrx)

for line in bbs:
    i = line[0]
    j = line[1]

    mtrx[i - 1][j - 1] += 1
    mtrx[i - 1][j] += 1
    mtrx[i - 1][j + 1] += 1

    mtrx[i][j - 1] += 1
    mtrx[i][j + 1] += 1

    mtrx[i + 1][j - 1] += 1
    mtrx[i + 1][j] += 1
    mtrx[i + 1][j + 1] += 1

for line in bbs:
    i = line[0]
    j = line[1]
    mtrx[i][j] = '*'

new_matrix = mtrx[1:-1]
for i_ln in range(0, n):
    new_matrix[i_ln] = new_matrix[i_ln][1:-1]
    print(*new_matrix[i_ln])
