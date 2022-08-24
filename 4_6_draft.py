alpha_list = []
with open('input.txt', 'r') as file_obj:

    for line in file_obj.readlines():
        alpha_list.append(line.rstrip())

    alpha_list = sorted(alpha_list)
    # print(alpha_list)

    current_name = ''
    current_product = ''
    counter = 0
    for i in range(0, len(alpha_list)):
        line = alpha_list[i].split()

        if current_name != line[0] or current_product != line[1]:
            if current_name != '' and current_product != '':
                print(current_product, counter)
            if current_name != line[0]:
                print(line[0] + ":")
                current_name = line[0]
            current_product = line[1]
            counter = 0

        counter += int(line[2])
    print(current_product, counter)








