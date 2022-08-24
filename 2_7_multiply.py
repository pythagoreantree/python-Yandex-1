input_list = [int(j) for j in input().split()]

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

def get_two_sorted(a, b):
    ts = (a, b)
    if a > b:
        ts = (b, a)
    return ' '.join([str(item) for item in ts])


if len(input_list) == 1:
    print(input_list[0])
elif len(input_list) == 2:
    print(get_two_sorted(input_list[0], input_list[1]))
else:
    minus_array = []
    plus_array = []
    for i in input_list:
        if i < 0:
            minus_array.append(i)
        elif i > 0:
            plus_array.append(i)
        else:
            minus_array.append(i)
            plus_array.append(i)

    if len(minus_array) > 1 and len(plus_array) > 1:
        min1, min2 = find_min2(minus_array)
        max1, max2 = find_max2(plus_array)

        if min1*min2 < max1*max2:
            print(get_two_sorted(max1, max2))
        else:
            print(get_two_sorted(min1, min2))
    elif len(minus_array) < 2 and len(plus_array) > 1:
        max1, max2 = find_max2(plus_array)
        print(get_two_sorted(max1, max2))
    elif len(plus_array) < 2 and len(minus_array) > 1:
        min1, min2 = find_min2(minus_array)
        print(get_two_sorted(min1, min2))




