k = int(input())
s = input()

prev_len = 0
oper_count = 0

for i in range(k, len(s)):
    if s[i] == s[i - k]:
        prev_len += 1
        oper_count += prev_len
    else:
        prev_len = 0

print(oper_count)

