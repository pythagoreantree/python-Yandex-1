import math


def rbinsearch(l, r, check, params):
    while l < r:
        mid = (l + r + 1) // 2
        if check(mid, params):
            l = mid
        else:
            r = mid - 1
    return l


def check_square(d, params):
    # print(d)
    x, y, tiles = params
    # print((x*y - (x - d*2)*(y - d*2)), tiles)
    # print("###################")
    return (x*y - (x - d*2)*(y - d*2)) <= tiles


n = int(input())
m = int(input())
t = int(input())
edge = min(math.floor(n/2), math.floor(m/2))
# print(edge)
ans = rbinsearch(0, edge, check_square, (n, m, t))
print(ans)

