n = int(input())
peak_pairs = []
for _ in range(n):
    x, y = map(int, input().split())
    peak_pairs.append((x, y))

m = int(input())
tracks = []
for _ in range(m):
    x, y = map(int, input().split())
    tracks.append((x, y))

heights = [0]*(n + 1)
anti_heights = [0]*(n + 1)
curr_y = 0
i = 1
for x, y in peak_pairs:
    delta_h = y - curr_y
    if delta_h > 0:
        heights[i] = heights[i-1] + delta_h
        anti_heights[i] = anti_heights[i-1]
    elif delta_h < 0:
        heights[i] = heights[i-1]
        anti_heights[i] = anti_heights[i-1] + abs(delta_h)
    else:
        heights[i] = heights[i-1]
        anti_heights[i] = anti_heights[i-1]
    curr_y = y
    i += 1

for start, end in tracks:
    if start <= end:
        print(heights[end] - heights[start])
    else:
        print(anti_heights[start] - anti_heights[end])








