a = int(input())
b = int(input())
c = int(input())

bc = b + c
ac = a + c
ab = a + b

if (a < bc) & (b < ac) & (c < ab):
    print('YES')
else:
    print('NO')
