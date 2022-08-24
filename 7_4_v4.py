n = int(input())
customers = []
for num in range(n):
    start, end = map(int, input().split())
    if end - start >= 5:
        customers.append((start, -1, num))
        customers.append((end - 5, 1, num))

customers.sort()

if len(customers) == 0:
    print(0, 1, 10)
elif len(customers) == 2:
    print(1, customers[0][0], customers[0][0] + 10)
else:
    max_count = 0
    first_interval_start = 0
    second_interval_start = 0
    first_adv_seen_by = set()

    for i in range(len(customers)):
        first_customer = customers[i]

        if first_customer[1] == -1:
            first_adv_seen_by.add(first_customer[2])
            if len(first_adv_seen_by) > max_count:
                max_count = len(first_adv_seen_by)
                first_interval_start = first_customer[0]
                second_interval_start = first_interval_start + 5

        second_adv_counter = 0

        for j in range(i + 1, len(customers)):
            second_customer = customers[j]

            if second_customer[1] == -1 and second_customer[2] not in first_adv_seen_by:
                second_adv_counter += 1
            if second_customer[0] - 5 >= first_customer[0] and len(first_adv_seen_by) + second_adv_counter > max_count:
                max_count = len(first_adv_seen_by) + second_adv_counter
                first_interval_start = first_customer[0]
                second_interval_start = second_customer[0]
            if second_customer[1] == 1 and second_customer[2] not in first_adv_seen_by:
                second_adv_counter -= 1

        if first_customer[1] == 1:
            first_adv_seen_by.remove(first_customer[2])

    print(max_count, first_interval_start, second_interval_start)
