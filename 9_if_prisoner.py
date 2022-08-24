a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


def sorted3(x, y, z):
    if x > y:
        x, y = y, x
    if y > z:
        y, z = z, y
    if x > y:
        x, y = y, x
    return x, y, z


def sorted2(x, y):
    if x > y:
        return y, x
    return x, y


a, b, c = sorted3(a, b, c)
d, e = sorted2(d, e)

if a <= d and b <= e:
    print('YES')
else:
    print('NO')
