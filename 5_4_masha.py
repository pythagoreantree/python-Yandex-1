n, r = map(int, input().split())
monuments = list(map(int, input().split()))

fp = 0
sp = 0
counter = 0
while sp < n:
    distance = monuments[sp] - monuments[fp]
    # print(distance)
    if distance > r:
        counter += (n - sp)
        fp += 1
    else:
        sp += 1
    # print(fp, sp)

print(counter)

