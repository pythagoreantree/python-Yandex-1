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
    max1, max2, max3 = find_max3(input_list)
    min1, min2 = find_min2(input_list)

    mult1 = max1*max2*max3
    mult2 = max1*min1*min2

    if mult1 > mult2:
        print(max1, max2, max3)
    else:
        print(max1, min1, min2)
