n = int(input())
customers = []
for _ in range(n):
    start, end = map(int, input().split())
    if end - start >= 5:
        customers.append((start, 1, end))
        customers.append((end, -1, start))

customers.sort()
print(customers)

customers_in_shop = 0
customers_on = set()

max1 = 0
max1_start = 0
max1_end = 0

for i in range(len(customers)):
    customer = customers[i]

    if customer[1] == 1:
        customers_in_shop += 1
        customers_on.add((customer[0], customer[2]))

    if customer[1] == -1:
        customers_in_shop -= 1
        customers_on.remove((customer[2], customer[0]))

    if customers_in_shop > 0:
        if customers_in_shop > max1 and (customer[0] >= max1_end or customer[0] == max1_start):
            max1 = customers_in_shop
            max1_start = customer[0]
            max1_end = max1_start + 5

        print(customer)
        print(customers_in_shop)
        print(max1, max1_start, max1_end)
    print('#####################')

max2 = 0
max2_start = 0
max2_end = 0

for i in range(len(customers)):
    customer = customers[i]

    if customer[1] == 1:
        customers_in_shop += 1
        customers_on.add((customer[0], customer[2]))

    if customer[1] == -1:
        customers_in_shop -= 1
        customers_on.remove((customer[2], customer[0]))

    if customers_in_shop > 0:
        if customers_in_shop > max2 and (customer[0] >= max2_end or customer[0] == max2_start):
            max2 = customers_in_shop
            max2_start = customer[0]
            max2_end = max2_start + 5

        print(customer)
        print(customers_in_shop)
        print(max2, max2_start, max2_end)
    print('#####################')

print(max1, max1_start, max1_end)
print(max2, max2_start, max2_end)







# customers_on = set()
# customers_in_shop = 0
# customers_who_watched_max1 = set()
# customers_who_watched_max2 = set()
#
# max1 = 0
# max1_start = 0
# max1_end = 0
#
# max2 = 0
# max2_start = 0
# max2_end = 0
#     if i > 0:
#         prev_customer = customers[i - 1]
#     else:
#         prev_customer = (0, 0, 0)
#     if i > 0 and 0 < customer[0] - prev_customer[0] < 5:
#         j = i - 1
#         while j > 0 and 0 < customer[0] - prev_customer[0] < 5:
#             prev_customer = customers[j - 1]
#             j -= 1
#     if customer[0] - prev_customer[0] >= 5:
#         print(customer[0], prev_customer[0])
#         if customers_in_shop > max1:
#             max2 = max1
#             max1 = customers_in_shop
#             max2_start = max1_start
#             max2_end = max1_end
#             max1_start = prev_customer[0]
#             max1_end = customer[0]
#             customers_who_watched_max2.clear()
#             customers_who_watched_max2.update(customers_who_watched_max1)
#             customers_who_watched_max1.clear()
#             customers_who_watched_max1.update(customers_on)
#         elif customers_in_shop > max2:
#             max2 = customers_in_shop
#             max2_start = prev_customer[0]
#             max2_end = customer[0]
#             customers_who_watched_max2.clear()
#             customers_who_watched_max2.update(customers_on)
#         print(max1, max2, max1_start, max1_end, max2_start, max2_end)
#         print(customers_who_watched_max1)
#         print(customers_who_watched_max2)
#         print('##############')
#     if customer[1] == -1:
#         customers_in_shop += 1
#         customers_on.add((customer[0], customer[2]))
#     if customer[1] == 1:
#         customers_in_shop -= 1
#         customers_on.remove((customer[2], customer[0]))
#
# if max2 == 0:
#     max2_start = max1_end + 1
#     max2_end = max2_start + 5
# all_customers_who_watched = set()
# all_customers_who_watched.update(customers_who_watched_max1)
# all_customers_who_watched.update(customers_who_watched_max2)
#
# if max1_start > max2_start:
#     max1_start, max2_start = max2_start, max1_start
# print(len(all_customers_who_watched), max1_start, max2_start)

# print(customers_who_watched_max1)
# print(customers_who_watched_max2)
# print(all_customers_who_watched)
# print(max1, max1_start, max1_end)
# print(max2, max2_start, max2_end)

# print(customers)


# print(max1, max2, max1_start, max1_end, max2_start, max2_end)
# print(customers_who_watched_max1)
# print(customers_who_watched_max2)
# print('##############')

# max1 = 0
# max_pointer1 = 0
# max_end_pointer1 = 0
# start_pointer = 0
# customers_num = 0

# customers_avail = set()
# customers_who_watched = set()
# all_customers_watched = set()

# for i in range(len(customers)):
#     customer = customers[i]
#     if customer[1] == 1:
#         start_pointer = customer[0]
#         customers_avail.add((customer[0], customer[2]))
#         customers_num += 1
#     if customer[1] == 0:
#         if customers_num > max1:
#             max1 = customers_num
#             max_pointer1 = start_pointer
#             max_end_pointer1 = customer[0]
#             customers_who_watched.clear()
#             customers_who_watched.update(customers_avail)
#             customers_avail.remove((customer[2], customer[0]))
#             customers_num -= 1


# print(max1)
# print(max_pointer1)
# print(max_end_pointer1)
# print(customers_who_watched)
# all_customers_watched.update(customers_who_watched)

# max2 = 0
# max_pointer2 = 0
# max_end_pointer2 = 0
# customers_avail.clear()
#
# for j in range(len(customers)):
#     customer = customers[j]
#     if customer[1] == 1:
#         start_pointer = customer[0]
#         customers_num += 1
#         customers_avail.add((customer[0], customer[2]))
#     if customer[1] == 0:
#         if customers_num > max2 and start_pointer != max_pointer1:
#             max2 = customers_num
#             max_pointer2 = start_pointer
#             max_end_pointer2 = customer[0]
#             customers_who_watched.clear()
#             customers_who_watched.update(customers_avail)
#         customers_avail.remove((customer[2], customer[0]))
#         customers_num -= 1
#
# if max2 == 0:
#     max_pointer2 = max_end_pointer1 + 1
#
# print(max2)
# print(max_pointer2)
# print(max_end_pointer2)
# print(customers_who_watched)
#
# all_customers_watched.update(customers_who_watched)
# print(all_customers_watched)
#
# print(len(all_customers_watched), max_pointer1, max_pointer2)

# FINAAALLLLL!!!!!
#
# n = int(input())
# customers = []
# for _ in range(n):
#     start, end = map(int, input().split())
#     if end - start >= 5:
#         customers.append((start, 1, end))
#         customers.append((end, -1, start))
#
# customers.sort()
# # print(customers)
#
# if len(customers) == 2:
#     print(1, customers[0][0], customers[1][0])
# else:
#     big_pull = set()
#     customers_in_shop = 0
#
#     customers_on = set()
#     periods_dict = {}
#
#     for i in range(len(customers)):
#         customer = customers[i]
#         print(customer)
#
#         customers_in_shop_before = customers_in_shop
#
#         if customer[1] == 1:
#             customers_in_shop += 1
#             customers_on.add((customer[0], customer[2]))
#         if customer[1] == -1:
#             customers_in_shop -= 1
#             customers_on.remove((customer[2], customer[0]))
#
#         if customers_in_shop_before > 0 and i > 0:
#             print('#1')
#             customer_before = customers[i - 1]
#             print('prev cust:', customer_before)
#             if customer[0] - customer_before[0] >= 5:
#                 local_set = set()
#                 local_set.update(customers_on)
#                 if customer[1] == -1:
#                     local_set.add((customer[2], customer[0]))
#                 elif customer[1] == 1:
#                     if (customer[0], customer[2]) in local_set:
#                         local_set.remove((customer[0], customer[2]))
#                 pair = (customer[0] - 5, customer[0])
#                 print(pair)
#                 print('>= 5 customers_on:', local_set)
#                 if pair not in periods_dict:
#                     periods_dict[pair] = set()
#                     periods_dict[pair].update(local_set)
#                 big_pull.add(pair)
#             else:
#                 j = 2
#                 local_set = set()
#                 local_set.update(customers_on)
#                 if customer[1] == -1:
#                     local_set.add((customer[2], customer[0]))
#                 elif customer[1] == 1:
#                     if (customer[0], customer[2]) in local_set:
#                         local_set.remove((customer[0], customer[2]))
#                 print('local_set before:', local_set)
#                 while customer[0] - customer_before[0] < 5 and (i - j >= 0):
#                     if customer_before[1] == 1 and (customer_before[0] != customer[0] - 5):
#                         local_set.remove((customer_before[0], customer_before[2]))
#                     customer_before = customers[i - j]
#                     j += 1
#                 print('local_set after:', local_set)
#                 if customer[0] - 5 > 0:
#                     pair = (customer[0] - 5, customer[0])
#                     print(pair)
#                     if pair not in periods_dict:
#                         periods_dict[pair] = set()
#                         periods_dict[pair].update(local_set)
#                     big_pull.add(pair)
#         print('##################')
#
#         if customers_in_shop > 0 and i < (len(customers) - 1):
#             print('#2')
#             next_customer = customers[i + 1]
#             print('next cust:', next_customer)
#             if next_customer[0] - customer[0] >= 5:
#                 pair = (customer[0], customer[0] + 5)
#                 print(pair)
#                 print('>= 5 customers_on:', customers_on)
#                 if pair not in periods_dict:
#                     periods_dict[pair] = set()
#                     periods_dict[pair].update(customers_on)
#                 big_pull.add(pair)
#             else:
#                 j = 2
#                 local_set = set()
#                 local_set.update(customers_on)
#                 print('local_set before:', local_set)
#                 while next_customer[0] - customer[0] < 5 and (i + j <= len(customers) - 1):
#                     if next_customer[1] == -1 and (next_customer[0] != customer[0] + 5):
#                         local_set.remove((next_customer[2], next_customer[0]))
#                     elif next_customer[1] == 1 and next_customer[0] == customer[0]:
#                         local_set.add((next_customer[0], next_customer[2]))
#                     next_customer = customers[i + j]
#                     j += 1
#                 print('local_set after:', local_set)
#                 if customer[0] + 5 <= customers[-1][0]:
#                     pair = (customer[0], customer[0] + 5)
#                     print('pair:', pair)
#                     if pair not in periods_dict:
#                         periods_dict[pair] = set()
#                         periods_dict[pair].update(local_set)
#                     big_pull.add(pair)
#
#         print('##################')
#         print(big_pull)
#         print(periods_dict)
#         print('########1########')
#
#     print(sorted(big_pull))
#     print(periods_dict)
#
#     print('########END########')
#
#     max_num = 0
#     first_advert = 0
#     second_advert = 0
#     for key1 in periods_dict.keys():
#         for key2 in periods_dict.keys():
#             print(key1, key2)
#             if key1 != key2 and (key1[1] <= key2[0] or key2[1]) <= key1[0]:
#                 k1_set = periods_dict[key1]
#                 counter = len(k1_set)
#                 for pair in periods_dict[key2]:
#                     if pair not in k1_set:
#                         counter += 1
#                 if counter > max_num:
#                     max_num = counter
#                     first_advert = key1[0]
#                     second_advert = key2[0]
#                 print(counter, max_num, first_advert, second_advert)
#                 print('##############')
#
#     print(max_num, first_advert, second_advert)














