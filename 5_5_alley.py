n, k = map(int, input().split())
trees = list(map(int, input().split()))

# k_sum = int(k*(k + 1)/2)
k_arr = [0]*(k + 1)
counter_nn = 0

fp = 0
sp = 0
pair = (0, n - 1)
while sp < n:
    while counter_nn < k and sp < n:
        t = trees[sp]
        c = k_arr[t]
        if c == 0:
            counter_nn += 1
        k_arr[t] += 1
        sp += 1
    while counter_nn == k:
        t0 = trees[fp]
        if (k_arr[t0] - 1) == 0:
            if (sp - fp) <= (pair[1] - pair[0] + 1):
                pair = (fp, sp - 1)
            counter_nn -= 1
        k_arr[t0] -= 1
        fp += 1
final_pair = pair[0] + 1, pair[1] + 1
print(*final_pair)








