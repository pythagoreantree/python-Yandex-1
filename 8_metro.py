a = int(input())
b = int(input())
n = int(input())
m = int(input())

xmin = n*1 + (n - 1)*a
xmax = n*1 + (n + 1)*a

ymin = m*1 + (m - 1)*b
ymax = m*1 + (m + 1)*b

maxmin = max(xmin, ymin)
minmax = min(xmax, ymax)

if maxmin > minmax:
    print(-1)
else:
    print(maxmin, minmax)
