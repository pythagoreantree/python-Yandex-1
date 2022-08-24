n = int(input())
shirts = list(map(int, input().split()))
m = int(input())
pants = list(map(int, input().split()))

fp = 0
sp = 0
min_delta = abs(shirts[fp] - pants[sp])
pair = (shirts[fp], pants[sp])
while fp < n and sp < m:
    delta = abs(shirts[fp] - pants[sp])
    if delta <= min_delta:
        min_delta = delta
        pair = (shirts[fp], pants[sp])
    if shirts[fp] <= pants[sp]:
        fp += 1
    else:
        sp += 1

print(*pair)

