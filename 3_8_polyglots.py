n = int(input())

arr = []
for _ in range(n):
    m = int(input())
    s = set()
    for _ in range(m):
        line = str(input())
        s.add(line)
    arr.append(s)

res1 = arr[0]
res2 = arr[0]
for i in range(1, len(arr)):
    res1 = res1.intersection(arr[i])
    res2 = res2.union(arr[i])

print(len(res1))
print(*res1, sep='\n')
print(len(res2))
print(*res2, sep='\n')



