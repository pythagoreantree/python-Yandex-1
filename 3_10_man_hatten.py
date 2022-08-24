t, d, n = map(int, input().split())
coords = []
for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))
# print(coords)


def create_field(pos, delta):
    minXpY, maxXpY, minXmY, maxXmY = pos
    return [minXpY - delta, maxXpY + delta, minXmY - delta, maxXmY + delta]


def get_possible_field(pos, nav):
    return [max(pos[0], nav[0]), min(pos[1], nav[1]), max(pos[2], nav[2]), min(pos[3], nav[3])]


position_field = (0, 0, 0, 0)
for crd in coords:
    position_field = create_field(position_field, t)
    x, y = crd[0], crd[1]
    navigator_field = create_field((x+y, x+y, x-y, x-y), d)
    position_field = get_possible_field(position_field, navigator_field)

dest_coords = []
for xpy in range(position_field[0], position_field[1]+1):
    for xmy in range(position_field[2], position_field[3]+1):
        if (xpy + xmy) % 2 == 0:
            x = (xpy + xmy) // 2
            y = xpy - x
            dest_coords.append((x, y))

print(len(dest_coords))
for crd in dest_coords:
    print(crd[0], crd[1])
