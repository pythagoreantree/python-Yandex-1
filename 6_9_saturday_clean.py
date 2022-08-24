def lbinsearch(left, right, check, params):
    while left < right:
        m = (left + right) // 2
        # print(left, r, m)
        if check(m, params):
            right = m
            # print("right", r)
        else:
            left = m + 1
            # print("left", left)
    return left


def check_groups_num(x, params):
    teams_num, stud_num, students = params
    teams_counter = 0
    ind = 0
    while ind + (stud_num - 1) < len(students):
        dh = students[ind + (stud_num - 1)] - students[ind]
        if dh <= x:
            teams_counter += 1
            ind += stud_num
        else:
            ind += 1
    # print(x, teams_counter, teams_num)
    # print('###################')
    return teams_counter >= teams_num


n, r, c = map(int, input().split())
heights = []
for _ in range(n):
    heights.append(int(input()))

heights.sort()
# print(heights)

max_delta = heights[len(heights)-1] - heights[0]
# print(max_delta)
ans = lbinsearch(0, max_delta, check_groups_num, (r, c, heights))
print(ans)
