n = int(input())

true_turtles = set()

for i in range(n):
    a, b = map(int, input().split())
    if a + b == n - 1 and a >= 0 and b >= 0:
        # s = str(a) + '_' + str(b)
        # print(a, b, s)
        true_turtles.add((a, b))

print(len(true_turtles))

