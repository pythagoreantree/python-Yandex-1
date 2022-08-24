with open('input.txt', 'r') as file_obj:
    words_d = {}
    list_of_counts = []
    for line in file_obj.readlines():
        words_list = line.split()
        for w in words_list:
            if w not in words_d:
                words_d[w] = 0
            list_of_counts.append(words_d[w])
            words_d[w] += 1
    print(*list_of_counts)

