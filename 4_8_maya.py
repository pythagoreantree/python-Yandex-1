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

# print(word_dict)

first_word = s[0:len(w)]
# print(first_word)
first_word_dict = get_chr_dict_from_string(first_word)

counter = 0
if word_dict == first_word_dict:
    counter += 1
for i in range(len(w), len(s)):
    last_symb = s[i]
    if last_symb not in first_word_dict:
        first_word_dict[last_symb] = 0
    first_word_dict[last_symb] += 1
    first_symb = s[(i-len(w))]
    first_word_dict[first_symb] -= 1
    if first_word_dict[first_symb] == 0:
        del first_word_dict[first_symb]
    if word_dict == first_word_dict:
        counter += 1
    # print(first_symb, last_symb)

print(counter)
