input_list = [int(j) for j in input().split()]


def find_min2(arr):
    lmin1 = min(arr[0], arr[1])
    lmin2 = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] < lmin1:
            lmin2 = lmin1
            lmin1 = arr[i]
        elif arr[i] < lmin2:
            lmin2 = arr[i]
    return lmin1, lmin2

def find_max2(arr):
    lmax1 = max(arr[0], arr[1])
    lmax2 = min(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] > lmax1:
            lmax2 = lmax1
            lmax1 = arr[i]
        elif arr[i] > lmax2:
            lmax2 = arr[i]
    return lmax1, lmax2

def define_maxxs(a, b, c):
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return c, b, a


# find 3 max
def find_max3(arr):
    lmax1, lmax2, lmax3 = define_maxxs(arr[0], arr[1], arr[2])
    for i in range(3, len(arr)):
        if arr[i] > lmax1:
            lmax3 = lmax2
            lmax2 = lmax1
            lmax1 = arr[i]
        elif arr[i] > lmax2:
            lmax3 = lmax2
            lmax2 = arr[i]
        elif arr[i] > lmax3:
            lmax3 = arr[i]
    return lmax1, lmax2, lmax3


if len(input_list) <= 3:
    print(' '.join([str(i) for i in input_list]))
else:
    minus_array = []
    plus_array = []
    hasnol = False
    for i in input_list:
        if i < 0:
            minus_array.append(i)
        elif i > 0:
            plus_array.append(i)
        else:
            hasnol = True
            minus_array.append(i)
            plus_array.append(i)

    aggregator = []

    if len(plus_array) >= 3:
        m1, m2, m3 = find_max3(plus_array)
        aggregator.append([m1*m2*m3, (m1, m2, m3)])

    if len(plus_array) >= 1 and len(minus_array) >= 2:
        m1 = 0
        if len(plus_array) == 1:
            m1 = plus_array[0]
        elif len(plus_array) == 2:
            if plus_array[0] > plus_array[1]:
                m1 = plus_array[0]
            else:
                m1 = plus_array[1]
        elif len(plus_array) >= 3:
            m1, m2, m3 = find_max3(plus_array)

        m4, m5 = find_min2(minus_array)
        aggregator.append([m1*m4*m5, (m1, m4, m5)])

    if not hasnol and len(plus_array) == 0 and len(minus_array) >= 3:
        m6, m7, m8 = find_max3(minus_array)
        # print(m6, m7, m8)
        aggregator.append([m6*m7*m8, (m6, m7, m8)])

    # print(aggregator)
    if len(aggregator) > 0:
        min_mult = aggregator[0][0]
        curr_record = aggregator[0]
        for record in range(0, len(aggregator)):
            if aggregator[record][0] > min_mult:
                min_mult = aggregator[record][0]
                curr_record = aggregator[record]

        print(' '.join([str(item) for item in curr_record[1]]))




