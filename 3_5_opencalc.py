a = set(map(int, input().split()))
n = int(input())

b = set()
while n != 0:
    d = n % 10
    n = n // 10
    if d not in a:
        b.add(d)

print(len(b))
