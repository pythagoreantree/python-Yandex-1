n, m = map(int, input().split())
a = set()
for _ in range(n):
    a.add(int(input()))

b = set()
for _ in range(m):
    b.add(int(input()))

g = a.intersection(b)
a_left = a.difference(g)
b_left = b.difference(g)

print(len(g))
print(*sorted(g))
print(len(a_left))
print(*sorted(a_left))
print(len(b_left))
print(*sorted(b_left))
