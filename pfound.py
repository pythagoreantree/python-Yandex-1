def pfound(top, vals, decay):
    final_sum = 1 * vals[0]
    for ind in range(2, top+1):
        final_sum += current_unit(ind, vals, decay) * vals[ind-1]
    return final_sum

def current_unit(top, vals, decay):
    # print(top)
    # print(vals)
    # print(decay)
    if top == 1:
        return 1
    return current_unit(top-1, vals,  decay) * (1 - vals[top-2]) * decay

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

f = open("output.txt", "w")
docs_decay = input().split()
doc_num = int(docs_decay[0])
decay = float(docs_decay[1])
rel_vals = input().split()
doc_values = []
for val in rel_vals:
    doc_values.append(float(val))
q_num = int(input())
while q_num > 0:
    list = input().split()
    i = int(list[0])
    j = int(list[1])
    top = min(doc_num, int(list[2]))
    # print(doc_values)
    pfound_before = round(pfound(top, doc_values, decay),9)
    # print(pfound_before)
    swapPositions(doc_values, i-1, j-1)
    # print(doc_values)
    pfound_after = round(pfound(top, doc_values, decay),9)
    print(pfound_after)
    swapPositions(doc_values, i-1, j-1)
    delta = abs(pfound_after - pfound_before)
    f.write("{:.9f}".format(delta))
    f.write('\n')
    pfound_before = 0.0
    pfound_after = 0.0
    q_num -= 1
f.close()

