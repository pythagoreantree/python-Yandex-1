# Дан текст.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

with open('input.txt', 'r') as file_obj:
    words_d = {}
    max_count = 0
    for line in file_obj.readlines():
        words_list = line.split()
        for w in words_list:
            if w not in words_d:
                words_d[w] = 0
            words_d[w] += 1
            if words_d[w] > max_count:
                max_count = words_d[w]
    list_of_max_words = []
    for key, value in words_d.items():
        if value == max_count:
            list_of_max_words.append(key)
    print(sorted(list_of_max_words)[0])
