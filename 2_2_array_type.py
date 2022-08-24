# def constant_seq(sequence):
#     current = sequence[0]
#     for i in range(1, len(sequence)):
#         if sequence[i] != current:
#             return False
#         else:
#             current = sequence[i]
#     return True
#
#
# def ascending_seq(sequence):
#     current = sequence[0]
#     for i in range(1, len(sequence)):
#         if sequence[i] <= current:
#             return False
#         else:
#             current = sequence[i]
#     return True
#
#
# def weakly_ascending_seq(sequence):
#     current = sequence[0]
#     for i in range(1, len(sequence)):
#         if sequence[i] < current:
#             return False
#         else:
#             current = sequence[i]
#     return True
#
#
# def descending_seq(sequence):
#     current = sequence[0]
#     for i in range(1, len(sequence)):
#         if sequence[i] >= current:
#             return False
#         else:
#             current = sequence[i]
#     return True
#
#
# def weakly_descending_seq(sequence):
#     current = sequence[0]
#     for i in range(1, len(sequence)):
#         if sequence[i] > current:
#             return False
#         else:
#             current = sequence[i]
#     return True


const = (-2*(10**9))
# const = 5
# print(const)

list_of_nums = []
while True:
    x = int(input())
    if x == const:
        break
    list_of_nums.append(x)
if len(list_of_nums) > 0:
    constant = True
    asc = True
    weakly_asc = True
    desc = True
    weakly_desc = True

    current = list_of_nums[0]
    for i in range(1, len(list_of_nums)):
        if list_of_nums[i] != current:
            constant = False
        if list_of_nums[i] <= current:
            asc = False
        if list_of_nums[i] < current:
            weakly_asc = False
        if list_of_nums[i] >= current:
            desc = False
        if list_of_nums[i] > current:
            weakly_desc = False
        current = list_of_nums[i]
    if constant:
        print('CONSTANT')
    elif asc:
        print('ASCENDING')
    elif weakly_asc:
        print('WEAKLY ASCENDING')
    elif desc:
        print('DESCENDING')
    elif weakly_desc:
        print('WEAKLY DESCENDING')
    else:
        print('RANDOM')

    # if constant_seq(list_of_nums):
    #     print('CONSTANT')
    # elif ascending_seq(list_of_nums):
    #     print('ASCENDING')
    # elif weakly_ascending_seq(list_of_nums):
    #     print('WEAKLY ASCENDING')
    # elif descending_seq(list_of_nums):
    #     print('DESCENDING')
    # elif weakly_descending_seq(list_of_nums):
    #     print('WEAKLY DESCENDING')
    # else:
    #     print('RANDOM')



