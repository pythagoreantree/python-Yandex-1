n, d = map(int, input().split())
dots = list(map(int, input().split()))

# print(sorted(dots))
classmates = []
for dot in dots:
    start = dot - d if dot - d > 0 else 0
    end = dot + d
    classmates.append((start, -1, dot))
    classmates.append((dot, 0, dot))
    classmates.append((end, 1, dot))

classmates.sort()
# print(classmates)

current_free_ticket = 1


classmates_in_area = 0
tickets = dict()
pointer = 1
# counter = 1
tickets_num = 0
ticket_nums = set()

for classmate in classmates:
    if classmate[1] == -1:
        classmates_in_area += 1
    if classmate[1] == 0:
        if classmates_in_area > 0:
            if pointer not in tickets.values():
                tickets_num += 1

            if pointer not in ticket_nums:
                tickets[classmate[2]] = pointer
                ticket_nums.add(pointer)
            else:
                counter = pointer
                while counter in ticket_nums:
                    counter += 1
                if counter not in tickets.values():
                    tickets_num += 1
                tickets[classmate[2]] = counter
                ticket_nums.add(counter)
            pointer += 1

    if classmate[1] == 1:
        if classmate[2] in tickets:
            new_free_ticket = tickets[classmate[2]]
            if new_free_ticket < pointer:
                pointer = new_free_ticket
            if new_free_ticket in ticket_nums:
                ticket_nums.remove(new_free_ticket)
        classmates_in_area -= 1

print(tickets_num)
for dot in dots:
    print(tickets[dot], end=' ')
