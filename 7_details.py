input_list = input().split()
n1, k1, m1 = map(int, input_list)


def get_details_num(n, k, m):
    hm_drafts = n // k
    first_phase_left = n % k
    # print(hm_drafts, first_phase_left)

    hm_details = k // m
    second_phase_left_one = k % m
    second_phase_left_all = hm_drafts * second_phase_left_one
    # print(hm_details, second_phase_left_one, second_phase_left_all)

    details_made = hm_drafts * hm_details
    # print(details)
    # print(first_phase_left + second_phase_left_all)
    left_all = first_phase_left + second_phase_left_all
    if left_all >= k:
        details_made += get_details_num(left_all, k, m)
    else:
        return details_made
    return details_made
    # return (hm_drafts * hm_details), (first_phase_left + second_phase_left_all)


if (m1 > k1) or (k1 > n1):
    print(0)
else:
    # left = n1
    # all_details = 0
    #
    # while left >= k1:
    #     details, materials_left = get_details_num(left, k1, m1)
    #     all_details += details
    #     left = materials_left
    #
    # print(all_details)
    print(get_details_num(n1, k1, m1))
