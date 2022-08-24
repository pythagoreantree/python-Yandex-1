arr_length = int(input())
nums = [int(i) for i in input().split()]
x = int(input())

arr_plus_nol = []
arr_minus_nol = []
# go through the array and divide into two
for n in nums:
    if n < 0:
        arr_minus_nol.append(n)
    elif n > 0:
        arr_plus_nol.append(n)
    else:
        arr_minus_nol.append(n)
        arr_plus_nol.append(n)


def closest_num(target_x, array):
    delta = abs(target_x - array[0])
    num = array[0]
    for i in range(1, len(array)):
        if abs(target_x - array[i]) < delta:
            delta = abs(target_x - array[i])
            num = array[i]
    return num


if x < 0:
    # search in minus_nol array
    if len(arr_minus_nol) > 0:
        print(closest_num(x, arr_minus_nol))
    elif len(arr_plus_nol) > 0:
        print(closest_num(x, arr_plus_nol))
elif x > 0:
    if len(arr_plus_nol) > 0:
        print(closest_num(x, arr_plus_nol))
    elif len(arr_minus_nol) > 0:
        print(closest_num(x, arr_minus_nol))
else:
    positive_closest = 0
    negative_closest = 0
    if len(arr_plus_nol) > 0:
        positive_closest = closest_num(x, arr_plus_nol)
    if len(arr_minus_nol) > 0:
        negative_closest = closest_num(x, arr_minus_nol)
    if positive_closest < negative_closest:
        print(positive_closest)
    else:
        print(negative_closest)


