def get_chr_dict_from_string(target_string):
    chr_set = {}
    for ind in range(0, len(target_string)):
        c = target_string[ind]
        if c not in chr_set:
            chr_set[c] = 0
        chr_set[c] += 1
    return chr_set

# def get_chr_set_from_string(target_string):
#     chr_set = set()
#     for ind in range(0, len(target_string)):
#         c = target_string[ind]
#         chr_set.add(c)
#     return chr_set

with open('input.txt', 'r') as file_obj:
    i = 0
    n, m, w, s = 0, 0, '', ''
    for line in file_obj.readlines():
        if i == 0:
            n, m = map(int, line.split())
        elif i == 1:
            w = str(line).rstrip()
        else:
            s = str(line).rstrip()
        i += 1

# alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# alpha_set = set()
# for symb in alphabet:
#     alpha_set.add(symb)
#     alpha_set.add(symb.lower())

# word_set = get_chr_set_from_string(w)
# not_in_set = alpha_set.difference(word_set)
word_dict = get_chr_dict_from_string(w)
# print(word_dict)
# print(get_chr_dict_from_string(w))
# print(word_set)
# print(alpha_set)
# print(*not_in_set)

counter = 0
start = 0
d1 = {}
while start < len(s) - len(w) + 1:
    d1.clear()
    for i in range(start, start+len(w)):
        symb = s[i]
        # print(symb)
        if symb not in d1:
            d1[symb] = 0
        d1[symb] += 1
    # print(word_dict)
    print(start, d1)
    if d1 == word_dict:
        counter += 1
        start += 1
    elif len(d1) == len(word_dict):
        max_num_gt = 0
        max_sym = ''
        for symb in word_dict.keys():
            if symb in d1 and d1[symb] > word_dict[symb] and d1[symb] > max_num_gt:
                max_num_gt = d1[symb]
                max_sym = symb
        for i in range(start, start + len(w)):
            if s[i] == max_sym:
                ind = i
        start = ind + 1
    else:
        start += 1
    # print(start)

    # if d1 != word_dict:
    #
    #     if len(d1) != len(word_dict):
    #         start += 1
    #     else:
    #         max_num_gt = 0
    #         max_sym = ''
    #         for symb in word_dict.keys():
    #             if symb in d1 and d1[symb] > word_dict[symb] and d1[symb] > max_num_gt:
    #                 max_num_gt = d1[symb]
    #                 max_sym = symb
    #         # print(max_num_gt)
    #         # print(symb)
    #         # print(s1.rfind(symb))
    #         start += s1.rfind(max_sym)
    #     print(start)
    # else:
    #     counter += 1

print(counter)







