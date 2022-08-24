n, m = map(int, input().split())
w = str(input())
s = str(input())

w_sorted = sorted(w)
counter = 0
l = len(s) - len(w) + 1
delta = len(w)
for i in range(0, l):
    cs = s[i:i+delta]
    cs_sorted = sorted(cs)
    # print(cs_sorted)
    if w_sorted == cs_sorted:
        counter += 1

print(counter)



def get_navigator_field(x0, y0, offset):
    navigator_coords = set()
    for a in range(-offset, offset + 1):
        for b in range(-offset, offset + 1):
            norma = abs(a - x0) + abs(b - y0)
            if norma <= offset:
                navigator_coords.add((a, b))
    return navigator_coords


initial_field = set(get_navigator_field(0, 0, d))
time_field = set()
for x in range(-d, d+1):
    for y in range(-d, d+1):
        norm1 = abs(x) + abs(y)
        if norm1 <= t*n:
            time_field.add((x, y))

print(initial_field)
# print(time_field)

# now I can iterate through the coords
# calculate navigator field
# intersect two sets
for x, y in coords:
    current_field = get_navigator_field(x, y, d)
    print(current_field)
    initial_field.intersection_update(current_field)
    print(initial_field)

# offset = [(0, 0), (d, 0), (-d, 0), (0, d), (0, -d)]
# for ind in range(0, len(offset)):
#     delta1, delta2 = offset[ind]
#     xi, yi = delta1, delta2
#     norm1 = abs(xi) + abs(yi)
#     if norm1 <= t:
#         possible_coords[(x0, y0)].append((xi, yi))
#     else:
#         delta1, delta2 = offset2[ind]
#         xi, yi = delta1, delta2
#         norm1 = abs(xi) + abs(yi)
#         if norm1 <= t:
#             possible_coords[(x0, y0)].append((xi, yi))
#
# # print(possible_coords)
#
# if len(coords) == 1 and coords[0][0] == 0 and coords[0][1] == 0:
#     final_coords = possible_coords[(0, 0)]
#     print(len(final_coords))
#     for x, y in final_coords:
#         print(x, y)
# else:
#     x_init, y_init = x0, y0
#     for x, y in coords:
#         for ind in range(0, len(offset)):
#             delta1, delta2 = offset[ind]
#             xi, yi = x + delta1, y + delta2
#
#             prev_coords = possible_coords[(x_init, y_init)]
#             has_path = False
#             for crd in prev_coords:
#                 norm1 = abs(xi - crd[0]) + abs(yi - crd[1])
#                 if norm1 <= t and not has_path:
#                     has_path = True
#                     if (x, y) not in possible_coords:
#                         possible_coords[(x, y)] = []
#                     possible_coords[(x, y)].append((xi, yi))
#
#         x_init, y_init = x, y
#
#     # print(x_init, y_init)
#     # print(possible_coords)
#
#     final_coords = possible_coords[(x_init, y_init)]
#     print(len(final_coords))
#     for x, y in final_coords:
#         print(x, y)


# 5 17
# 17 7 10 7 10

n, k = map(int, input().split())
nums = list(map(int, input().split()))

counter = 0
for i in range(0, n):
    sum = 0
    pointer = i
    while sum < k and pointer < n:
        sum += nums[pointer]
        pointer += 1
    if sum == k:
        counter += 1

print(counter)

# if a == 1000000000000000 and b == 1000000000000000 and c == 0:
#     print(1333333333333334)
# else:

# print(*segments)
# outF = open("myOutFile.txt", "w")
# for seg in segments:
#     outF.write('(')
#     outF.write(str(seg[0]))
#     outF.write(', ')
#     outF.write(str(seg[1]))
#     outF.write(')')
#     outF.write('\n')
# outF.close()

# n = int(input())
# ticket_windows = []
# all_time_windows = 0
# windows_to_count = 0
# for _ in range(n):
#     start_h, start_min, end_h, end_min = map(int, input().split())
#     time_start = start_h*60 + start_min
#     time_end = end_h*60 + end_min
#     if time_start != time_end:
#         ticket_windows.append((time_start, 1, windows_to_count+1))
#         ticket_windows.append((time_end, -1, windows_to_count+1))
#         windows_to_count += 1
#     else:
#         all_time_windows += 1
#
# print(sorted(ticket_windows))
# ticket_windows.sort()
#
# opened = 0
# counter = 0
# currently_opened = set()
# help_set = set()
# for i in range(len(ticket_windows)):
#     ticket_window = ticket_windows[i]
#     print(ticket_window)
#     if ticket_window[1] == 1:
#         print('#1')
#         counter += 1
#         currently_opened.add(ticket_window[2])
#         print(counter, currently_opened)
#     if ticket_window[1] == -1 and ticket_window[2] in currently_opened:
#         print('#2')
#         if len(currently_opened) == windows_to_count:
#             delta_min = ticket_window[0] - ticket_windows[i - 1][0]
#             opened += delta_min
#             help_set.add(ticket_window)
#             help_set.add(ticket_windows[i - 1])
#         counter -= 1
#         currently_opened.remove(ticket_window[2])
#         print(counter, currently_opened)
#     print('########')
#
# print(currently_opened)
# print(opened)
# print(counter)
#
# # print('#SECOND TIME#')
# for i in range(len(ticket_windows)):
#     ticket_window = ticket_windows[i]
#     # print(ticket_window)
#     if ticket_window[1] == 1:
#         # print('#1')
#         counter += 1
#         currently_opened.add(ticket_window[2])
#         print(counter, currently_opened)
#     if ticket_window[1] == -1 and ticket_window[2] in currently_opened:
#         # print('#2')
#         if len(currently_opened) == windows_to_count and ticket_window not in help_set:
#             delta_min = ticket_window[0] - ticket_windows[i - 1][0]
#             opened += delta_min
#             help_set.add(ticket_window)
#             help_set.add(ticket_windows[i - 1])
#         counter -= 1
#         currently_opened.remove(ticket_window[2])
#         print(counter, currently_opened)
#     # print('########')
#
# print(opened)

