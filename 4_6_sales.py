# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alpha_dict = {}
with open('input.txt', 'r') as file_obj:
    # customers = {}
    for line in file_obj.readlines():
        customer = line.split()

        name = customer[0]
        if name not in alpha_dict:
            alpha_dict[name] = []
        alpha_dict[name].append((customer[1], customer[2]))

        # if (customer[0], customer[1]) not in customers:
        #     customers[(customer[0], customer[1])] = 0
        # customers[(customer[0], customer[1])] += int(customer[2])
    # print(alpha_dict)
    # print(sorted(customers))
    # for cust in sorted(customers):
    #     print(cust[0] + ":")
    #     print(cust[1], customers[cust])

    d = {}
    for customer in sorted(alpha_dict.keys()):
        product = alpha_dict[customer]
        for p in product:
            if p[0] not in d:
                d[p[0]] = 0
            d[p[0]] += int(p[1])

        print(customer + ":")
        for i in sorted(d.keys()):
            print(i, d[i])
        d.clear()






    # for line in file_obj.readlines():
    #     buyer = line.split()
    #     if buyer[0] not in buyers_base:
    #         buyers_base[buyer[0]] = {}
    #     buyer_goods = buyers_base[buyer[0]]
    #     if buyer[1] not in buyer_goods:
    #         buyer_goods[buyer[1]] = 0
    #     buyer_goods[buyer[1]] += int(buyer[2])
    #     # buyers_base[buyer[0]] = goods
    # for customer in sorted(buyers_base.keys()):
    #     print(customer + ':')
    #     for k in sorted(buyers_base[customer].keys()):
    #         print(k, buyers_base[customer][k])



