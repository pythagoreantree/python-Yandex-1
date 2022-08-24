with open('input.txt', 'r') as file_obj:
    i = 0
    n, m = 0, 0
    segments = []
    # raw_segments = []
    dots = {}
    dots_dict = {}
    for line in file_obj.readlines():
        if i == 0:
            n, m = map(int, line.split())
        elif 1 <= i <= n:
            start, end = map(int, line.split())
            if start <= end:
                segments.append((start, -1))
                segments.append((end, 1))
            else:
                segments.append((end, -1))
                segments.append((start, 1))
            # raw_segments.append((start, end))
        else:
            dots = list(map(int, line.split()))
            for dot in dots:
                segments.append((dot, 0))
                dots_dict[dot] = 0
        i += 1

segments.sort()

res = []
seg_count = 0
for i in range(len(segments)):
    segment = segments[i]

    if segment[1] == 0:
        dots_dict[segment[0]] = seg_count
    if segment[1] == -1:
        seg_count += 1
    if segment[1] == 1 and seg_count > 0:
        seg_count -= 1

for dot in dots:
    res.append(dots_dict[dot])
print(*res)

# j = 0
# outF = open("myOutFile.txt", "w")
# for dot in dots:
#   outF.write(str(dots_dict[dot]))
#   outF.write(' ')
#   j += 1
# outF.close()
#
# print(j)