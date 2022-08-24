def is_in_list(x, seq):
    left = 0
    r = len(seq)
    while left < r:
        m = (left + r) // 2
        # print(left, r, m)
        if seq[m] >= x:
            r = m
            # print("right", r)
        else:
            left = m + 1
            # print("left", left)
    if len(seq) <= left or seq[left] != x:
        return False
    else:
        return True


n, k = map(int, input().split())
first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

first_list = sorted(first_list)
for num in second_list:
    if is_in_list(num, first_list):
        print("YES")
    else:
        print("NO")
