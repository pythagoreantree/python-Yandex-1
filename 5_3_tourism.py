def get_line(x1, y1, x2, y2):
    if x1 == 0 and y1 == 0 and x2 != 0 and y2 != 0:
        bi = 0
        ki = y2/x2
        return ki, bi
    elif x1 != 0 and y1 != 0 and x2 == 0 and y2 == 0:
        bi = 0
        ki = y1/x1
        return ki, bi
    else:
        if x1 != 0:
            bi = (y2 * x1 - y1 * x2) / (x1 - x2)
            ki = (y1 - bi) / x1
            return ki, bi
        elif x2 != 0:
            bi = (y1 * x2 - x1 * y2)/(x2 - x1)
            ki = (y2 - bi) / x2
            return ki, bi
    return 0, 0


n = int(input())
peak_pairs = []
for _ in range(n):
    x, y = map(int, input().split())
    peak_pairs.append((x, y))

m = int(input())
tracks = []
for _ in range(m):
    x, y = map(int, input().split())
    if x > y:
        x, y = y, x
    tracks.append((x, y))

prev_x, prev_y = 0, 0
heights = [0]
curr_y = 0
s = 0
for x, y in peak_pairs:
    # print(prev_x, prev_y, x, y)
    k, b = get_line(prev_x, prev_y, x, y)
    # print(k, b)
    # print("")

    delta_h = y - curr_y if k >= 0 else 0
    s += delta_h
    heights.append(s)
    curr_y = y
    prev_x, prev_y = x, y

# print(len(heights))
# print(heights)

for start, end in tracks:
    print(int(heights[end] - heights[start]))





