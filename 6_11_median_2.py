def gensequence(l, x1, d1, a, c, m):
    sequence = [x1]
    d = d1
    for _ in range(l - 1):
        # print(sequence[-1], d)
        element = sequence[-1] + d
        sequence.append(element)
        d = (a*d + c) % m
        # print(element, d)
        # print('###########')
    return sequence


def lbinsearch(left, right, check, params):
    while left < right:
        mbs = (left + right) // 2
        if check(mbs, params):
            right = mbs
        else:
            left = mbs + 1
    return left


def check_is_ge(ind, params):
    seq, x = params
    return seq[ind] >= x


def count_left_elems(seq, x):
    ans = lbinsearch(0, len(seq) - 1, check_is_ge, (seq, x))
    if seq[ans] < x:
        return len(seq)
    return ans


def count_right_elems(seq, x):
    return len(seq) - count_left_elems(seq, x + 1)


def get_left_median(seq1, seq2):
    left = min(seq1[0], seq2[0])
    right = max(seq1[-1], seq2[-1])
    seq_len = len(seq1)
    while left < right:
        mid = (left + right) // 2
        left_count = count_left_elems(seq1, mid) + count_left_elems(seq2, mid)
        right_count = count_right_elems(seq1, mid) + count_right_elems(seq2, mid)
        if left_count <= seq_len - 1 and right_count <= seq_len:
            return mid
        if right_count > seq_len:
            left = mid + 1
        if left_count > seq_len - 1:
            right = mid - 1
    return left


n, l = map(int, input().split())
sequences = []
for _ in range(n):
    x1, d1, a, c, m = map(int, input().split())
    sequences.append(gensequence(l, x1, d1, a, c, m))

# print(sequences)
for i in range(n):
    for j in range(i + 1, n):
        left_median = get_left_median(sequences[i], sequences[j])
        print(left_median)
