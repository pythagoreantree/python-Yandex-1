a, b, c, d = map(int, input().split())


def lw(x, y):
    if x < y:
        return x, y
    else:
        return y, x


def square(x, y):
    return x * y


w1, l1 = lw(a, b)
w2, l2 = lw(c, d)

sqrs = []

v1_x = w1 + w2
v1_y = l1 if l1 >= l2 else l2
s1 = square(v1_x, v1_y)
sqrs.append([s1, (v1_x, v1_y)])
smin = s1

v2_x = l1 + w2
v2_y = w1 if w1 >= l2 else l2
s2 = square(v2_x, v2_y)
sqrs.append([s2, (v2_x, v2_y)])
if s2 < smin:
    smin = s2

v3_x = l2 + w1
v3_y = w2 if w2 >= l1 else l1
s3 = square(v3_x, v3_y)
sqrs.append([s3, (v3_x, v3_y)])
if s3 < smin:
    smin = s3

v4_x = l1 + l2
v4_y = w1 if w1 >= w2 else w2
s4 = square(v4_x, v4_y)
sqrs.append([s4, (v4_x, v4_y)])
if s4 < smin:
    smin = s4


def get_table_size(minsq, list):
    for s in list:
        # print(s)
        if s[0] == minsq:
            table_size = s[1]
            return table_size
    return 0, 0


stable = get_table_size(smin, sqrs)
print(stable[0], stable[1])
