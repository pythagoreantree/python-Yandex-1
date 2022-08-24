def search_nearest(x, seq):
    left, right = -1, len(seq)
    while right - left > 1:
        middle = (left + right) // 2
        if seq[middle] <= x:
            left = middle
        else:
            right = middle

    inf = int(1e18)
    left_delta = inf if -1 == left else x - seq[left]
    right_delta = inf if len(seq) == right else seq[right] - x
    ans = seq[left] if left_delta <= right_delta else seq[right]
    print(ans)


n, k = map(int, input().split())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

first_list = sorted(first_list)
for num in second_list:
    search_nearest(num, first_list)
