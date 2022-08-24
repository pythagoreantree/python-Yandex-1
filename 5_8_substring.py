n, k = map(int, input().split())
s = input()

d = {}
fp = 0
sp = 0

max_start = 0
max_len = 0

for i in range(len(s)):
    current_symbol = s[i]
    if current_symbol not in d:
        d[current_symbol] = 0
uniq_symb_counter = len(d.keys())
uniq_symb_in_str = 0
full_string = False

while sp < len(s):
    no_overload = True
    while sp < len(s) and no_overload:
        current_symbol = s[sp]
        if d[current_symbol] + 1 > k:
            no_overload = False
        else:
            d[current_symbol] += 1
            if d[current_symbol] == 1:
                uniq_symb_in_str += 1
                if uniq_symb_in_str == uniq_symb_counter:
                    full_string = True
            sp += 1
    if full_string and (sp - fp) > max_len:
        max_start = fp
        max_len = sp - fp
    while fp <= sp and (d[current_symbol] + 1) > k:
        first_symbol = s[fp]
        d[first_symbol] -= 1
        if d[first_symbol] == 0:
            uniq_symb_in_str -= 1
            full_string = False
        fp += 1

print(max_len, max_start + 1)



