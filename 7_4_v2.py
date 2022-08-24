n = int(input())
customers = []
custom_num = 1
for _ in range(n):
    start, end = map(int, input().split())
    if end - start >= 5:
        customers.append((start, 1, end, custom_num))
        customers.append((end, -1, start, custom_num))
    custom_num += 1

customers.sort()
# print(customers)

if len(customers) == 2:
    print(1, customers[0][0], customers[1][0])
else:
    big_pull = set()
    customers_in_shop = 0

    customers_on = set()
    periods_dict = {}

    for i in range(len(customers)):
        customer = customers[i]

        # if customer[1] == 1 and customer[0] < 48 and 53 < customer[2]:
        #     print(customer)
        #     test_set.add(customer)
        # if customer[1] == -1 and customer[2] < 48 and 53 < customer[0]:
        #     print(customer)
        #     test_set.add(customer)

        customers_in_shop_before = customers_in_shop

        if customer[1] == 1:
            customers_in_shop += 1
            customers_on.add((customer[0], customer[2], customer[3]))
        if customer[1] == -1:
            customers_in_shop -= 1
            if (customer[2], customer[0], customer[3]) in customers_on:
                customers_on.remove((customer[2], customer[0], customer[3]))

        if customers_in_shop_before > 0 and i > 0:
            customer_before = customers[i - 1]
            if customer[0] - customer_before[0] >= 5:
                local_set = set()
                local_set.update(customers_on)
                if customer[1] == -1:
                    local_set.add((customer[2], customer[0], customer[3]))
                elif customer[1] == 1:
                    if (customer[0], customer[2], customer[3]) in local_set:
                        local_set.remove((customer[0], customer[2], customer[3]))
                pair = (customer[0] - 5, customer[0])
                if pair not in periods_dict:
                    periods_dict[pair] = set()
                    periods_dict[pair].update(local_set)
                big_pull.add(pair)
            else:
                j = 2
                local_set = set()
                local_set.update(customers_on)
                if customer[1] == -1:
                    local_set.add((customer[2], customer[0], customer[3]))
                elif customer[1] == 1:
                    if (customer[0], customer[2], customer[3]) in local_set:
                        local_set.remove((customer[0], customer[2], customer[3]))
                while customer[0] - customer_before[0] < 5 and (i - j >= 0):
                    if customer_before[1] == 1:
                        if (customer_before[0], customer_before[2], customer_before[3]) in local_set:
                            local_set.remove((customer_before[0], customer_before[2], customer_before[3]))
                    customer_before = customers[i - j]
                    j += 1
                if customer[0] - 5 >= 0:
                    pair = (customer[0] - 5, customer[0])
                    if pair not in periods_dict:
                        periods_dict[pair] = set()
                        periods_dict[pair].update(local_set)
                    big_pull.add(pair)

        if customers_in_shop > 0 and i < (len(customers) - 1):
            next_customer = customers[i + 1]
            if next_customer[0] - customer[0] >= 5:
                pair = (customer[0], customer[0] + 5)
                if pair not in periods_dict:
                    periods_dict[pair] = set()
                    periods_dict[pair].update(customers_on)
                big_pull.add(pair)
            else:
                j = 2
                local_set = set()
                local_set.update(customers_on)
                while next_customer[0] - customer[0] < 5 and (i + j <= len(customers) - 1):
                    if next_customer[1] == -1:
                        if (next_customer[2], next_customer[0], next_customer[3]) in local_set:
                            local_set.remove((next_customer[2], next_customer[0], next_customer[3]))
                    elif next_customer[1] == 1 and next_customer[0] == customer[0]:
                        local_set.add((next_customer[0], next_customer[2], next_customer[3]))
                    next_customer = customers[i + j]
                    j += 1
                if customer[0] + 5 <= customers[-1][0]:
                    pair = (customer[0], customer[0] + 5)
                    if pair not in periods_dict:
                        periods_dict[pair] = set()
                        periods_dict[pair].update(local_set)
                    big_pull.add(pair)

    # print(periods_dict)
    max_num = 0
    first_advert = 0
    second_advert = 0

    # print(len(periods_dict.keys()))
    for key1 in periods_dict.keys():
        for key2 in periods_dict.keys():
            if (key1 == key2) or (key1[1] <= key2[0]) or (key2[1] <= key1[0]):
                k1_set = periods_dict[key1]
                k2_set = periods_dict[key2]
                diff = k2_set.difference(k1_set)
                counter = len(k1_set) + len(diff)
                if counter > max_num:
                    max_num = counter
                    first_advert = key1[0]
                    second_advert = key2[0]

    if first_advert == second_advert:
        for key in periods_dict.keys():
            if key[1] <= first_advert or key[0] >= (first_advert + 5):
                second_advert = key[0]
    if first_advert == second_advert:
        second_advert = first_advert + 5

    print(max_num, first_advert, second_advert)
