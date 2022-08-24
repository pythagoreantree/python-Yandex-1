s1 = str(input())
s2 = str(input())

pairs = set()
for i in range(len(s2) - 1):
    pair = s2[i:i+2]
    pairs.add(pair)

counter = 0
for i in range(len(s1) - 1):
    pair = s1[i:i+2]
    if pair in pairs:
        counter += 1

print(counter)