def rbinsearch(l, r, check, params):
    while l < r:
        m = (l + r + 1) // 2
        if check(m, params):
            l = m
        else:
            r = m - 1
    return l


def check_additional_width(d, params):
    # print(d)
    cont_num, w_cont, h_cont, w_field, h_field = params
    cont_new_w = w_cont + d*2
    cont_new_h = h_cont + d*2
    # print(cont_new_w, cont_new_h)

    cols_h = w_field // cont_new_w
    rows_h = h_field // cont_new_h
    # print(cols_h, rows_h)
    hor_oriented_ok = cols_h*rows_h >= n
    # print(hor_oriented_ok)

    cols_w = w_field // cont_new_h
    rows_w = h_field // cont_new_w
    # print(cols_w, rows_w)
    ver_oriented_ok = cols_w*rows_w >= n
    # print(ver_oriented_ok)
    # print("##############")
    return hor_oriented_ok or ver_oriented_ok


n, a, b, w, h = map(int, input().split())
max_axis = w if h < w else h
# print(max_axis)
ans = rbinsearch(0, max_axis, check_additional_width, (n, a, b, w, h))
print(ans)
