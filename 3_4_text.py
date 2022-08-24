import sys

a = set()
for line in sys.stdin:
    f_line = line.replace('\n', '')
    words_list = f_line.split()
    for word in words_list:
        a.add(word)

print(len(a))

