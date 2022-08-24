n, m = map(int, input().split())

events = []
for _ in range(m):
    start, end = map(int, input().split())
    if start != end:
        events.append((start, -1))
        events.append((end, 1))
    else:
        events.append((start, 0))
events.sort()

# print(events)
teachers = 0
desks = 0
prev_len = -1
for i in range(len(events)):
    event = events[i]
    # print(event)
    # print(i, event)
    if teachers == 0 and event[1] == 0:
        desks += 1
        # print('0 d + 1:', desks)

    if event[1] == -1:
        teachers += 1
        # print('t + 1:', teachers)

    if teachers > 0 and event[1] != 0:
        if prev_len == -1:
            desks += 1
        else:
            if event[0] != prev_len:
                desks += event[0] - prev_len
        prev_len = event[0]
        # print('d + 1:', desks)

    if event[1] == 1:
        teachers -= 1
        # print('t - 1:', teachers)

    if teachers == 0 and event[1] != 0:
        prev_len = 0
    # print(prev_len)
    # print('###########')

# print(desks)
# print('######')
# print(n, desks)
print(n - desks)
