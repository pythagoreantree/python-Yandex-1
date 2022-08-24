n = int(input())
customers = []
customer_segs = []
for num in range(n):
    start, end = map(int, input().split())
    if end - start >= 5:
        customers.append((start, 1, end, num + 1))
        customers.append((end, -1, start, num + 1))
        customer_segs.append((start, end, num + 1))

customers.sort()

if len(customers) == 2:
    print(1, customers[0][0], customers[1][0])
else:

    max_count = 0
    first_interval_start = 0
    second_interval_start = 0
    for i in range(len(customers)):
        first_customer = customers[i]

        if first_customer[1] == 1:

            first_adv_seen_by = set()

            for seg in customer_segs:
                if seg[0] <= first_customer[0] and first_customer[0] + 5 <= seg[1]:
                    first_adv_seen_by.add(seg[2])

            # print(first_adv_seen_by)

            for j in range(i + 1, len(customers)):
                second_customer = customers[j]

                second_counter = 0
                if second_customer[1] == 1:

                    start_index = second_customer[2] - 5
                    end_index = second_customer[2]

                    k = i + 1
                    next_customer = customers[k]
                    while k + 1 < len(customers) and next_customer[0] <= end_index:
                        if next_customer[1] == 1 and first_customer[0] < next_customer[0] <= start_index and next_customer[2] >= end_index:
                            second_counter += 1
                        k += 1
                        next_customer = customers[k]

                    if len(first_adv_seen_by) + second_counter > max_count:
                        max_count = len(first_adv_seen_by) + second_counter
                        if start_index < first_customer[0]:
                            first_interval_start = second_customer[2] - 5
                            second_interval_start = first_customer[0]
                        elif first_customer[0] == second_customer[2] - 5:
                            first_interval_start = first_customer[0]
                            second_interval_start = first_interval_start + 5
                        else:
                            first_interval_start = first_customer[0]
                            second_interval_start = second_customer[2] - 5
                    # print(max_count)

    print(max_count, first_interval_start, second_interval_start)

