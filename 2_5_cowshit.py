n = int(input())
throw_lengths = list(map(int, input().split()))

# print(sorted(throw_lengths, reverse=True))
maxi = 0
for i in throw_lengths:
    if i > maxi:
        maxi = i

# vasily_lengths = []
max_been = False
max_vasya = 0
# print(maxi)
for i in range(len(throw_lengths)):
    first_cond = (throw_lengths[i] % 10 == 5)
    second_cond = max_been
    third_cond = (i != (len(throw_lengths)-1) and throw_lengths[i + 1] < throw_lengths[i])
    edge_cond = (i != 0)
    # print(first_cond, second_cond, third_cond, edge_cond)
    if first_cond and second_cond and third_cond and edge_cond:
        if throw_lengths[i] > max_vasya:
            max_vasya = throw_lengths[i]
        # vasily_lengths.append(throw_lengths[i])
    if throw_lengths[i] == maxi:
        max_been = True

# print(vasily_lengths)
if max_vasya == 0:
    print(0)
else:
    counter = 0
    for tl in throw_lengths:
        if tl > max_vasya:
            counter += 1

    # print(counters)
    # minc = counters[0]
    # for c in counters:
    #     if c < minc:
    #        minc = c

    print(counter + 1)

