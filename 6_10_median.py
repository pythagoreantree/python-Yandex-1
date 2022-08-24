n, l = map(int, input().split())
arr_of_sequences = []
for _ in range(n):
    seq = list(map(int, input().split()))
    arr_of_sequences.append(seq)

# print(arr_of_sequences)
for i in range(len(arr_of_sequences)):
    for j in range(i + 1, len(arr_of_sequences)):
        seq1 = arr_of_sequences[i]
        seq2 = arr_of_sequences[j]
        fp = 0
        sp = 0
        counter = 0
        curr_value = min(seq1[0], seq2[0])
        while counter < l:
            if seq1[fp] < seq2[sp]:
                curr_value = seq1[fp]
                fp += 1
            else:
                curr_value = seq2[sp]
                sp += 1
            counter += 1
        print(curr_value)

