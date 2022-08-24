n = int(input())
available_pressings = list(map(int, input().split()))
m = int(input())
pressings = list(map(int, input().split()))
# 1 50 3 4 3
# 1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5

for p in pressings:
    available_pressings[p - 1] -= 1

for p in available_pressings:
    if p < 0:
        print('YES')
    else:
        print('NO')
