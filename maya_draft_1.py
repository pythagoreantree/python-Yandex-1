def get_chr_dict_from_string(target_string):
    chr_set = {}
    for indx in range(0, len(target_string)):
        c = target_string[indx]
        if c not in chr_set:
            chr_set[c] = 0
        chr_set[c] += 1
    return chr_set

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

word_dict = get_chr_dict_from_string(w)

counter = 0
start = 0
d1 = {}
while start < len(s) - len(w) + 1:
    d1.clear()
    for i in range(start, start+len(w)):
        symb = s[i]
        if symb not in d1:
            d1[symb] = 0
        d1[symb] += 1
    # print(start)
    # print(d1)
    # print(word_dict)
    if d1 == word_dict:
        counter += 1
    elif len(d1) == len(word_dict):
        max_num_gt = 0
        max_sym = ''
        for symb in word_dict.keys():
            if symb in d1 and d1[symb] > word_dict[symb] and d1[symb] > max_num_gt:
                max_num_gt = d1[symb]
                max_sym = symb
        if max_sym != '':
            ind = 0
            for i in range(start, start + len(w)):
                if s[i] == max_sym:
                    ind = i
                    break
            start = ind
    start += 1
    # print(start)
print(counter)