n = int(input())
ticket_windows = []
all_time_windows = 0
windows_to_count = 0
for _ in range(n):
    start_h, start_min, end_h, end_min = map(int, input().split())
    time_start = start_h*60 + start_min
    time_end = end_h*60 + end_min
    if time_start != time_end:
        ticket_windows.append((time_start, 1, windows_to_count+1))
        ticket_windows.append((time_end, -1, windows_to_count+1))
        windows_to_count += 1
    else:
        all_time_windows += 1

if len(ticket_windows) == 0 and all_time_windows > 0:
    print(1440)
else:
    # print(sorted(ticket_windows))
    ticket_windows.sort()

    opened = 0
    counter = 0
    currently_opened = set()
    minutes_after_first_circle = 0

    for i in range(len(ticket_windows)):
        ticket_window = ticket_windows[i]
        # print(ticket_window)
        if ticket_window[1] == 1:
            counter += 1
            currently_opened.add(ticket_window[2])
        if ticket_window[1] == -1 and ticket_window[2] in currently_opened:
            if len(currently_opened) == windows_to_count:
                delta_min = ticket_window[0] - ticket_windows[i - 1][0]
                opened += delta_min
            counter -= 1
            currently_opened.remove(ticket_window[2])

    minutes_after_first_circle = opened
    # print(currently_opened)
    # print(opened)

    for i in range(len(ticket_windows)):
        ticket_window = ticket_windows[i]
        # print(ticket_window)
        if ticket_window[1] == 1:
            counter += 1
            currently_opened.add(ticket_window[2])
        if ticket_window[1] == -1 and ticket_window[2] in currently_opened:
            if len(currently_opened) == windows_to_count:
                if ticket_window[0] < ticket_windows[i - 1][0]:
                    opened += (1440 - ticket_windows[i - 1][0])
                    opened += ticket_window[0]
                else:
                    opened += ticket_window[0] - ticket_windows[i - 1][0]
            counter -= 1
            currently_opened.remove(ticket_window[2])

    print(opened - minutes_after_first_circle)
