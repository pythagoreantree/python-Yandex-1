def get_base_pairs(genom):
    d = {}
    for i in range(len(genom) - 1):
        first_letter = genom[i:i+1]
        pair = genom[i:i+2]
        if first_letter not in d:
            d[first_letter] = {}
        if pair not in d[first_letter]:
            d[first_letter][pair] = 0
        d[first_letter][pair] += 1
    return d


s1 = str(input())
s2 = str(input())

bp1 = get_base_pairs(s1)
bp2 = get_base_pairs(s2)

min_len = len(bp1) if len(bp1) < len(bp2) else len(bp2)

common_ltrs = set()
for ltr in bp1.keys():
    if ltr in bp2:
        common_ltrs.add(ltr)

# print(common_ltrs)

common_counter = 0
for ltr in common_ltrs:
    gns1 = bp1.get(ltr)
    gns2 = bp2.get(ltr)
    for item in gns1.keys():
        if item in gns2.keys():
            common_counter += gns1[item]*gns2[item]

print(common_counter)

# print(bp1)
# print(bp2)