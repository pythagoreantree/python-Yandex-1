def check_board(x, params):
    w, h, n = params
    return (x // w) * (x // h) >= n


def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    print(l)


w, h, n = map(int, input().split())
mxcube = w*n if w > h else h*n
# print(0, n, mxcube)
lbinsearch(1, mxcube, check_board, (w, h, n))


