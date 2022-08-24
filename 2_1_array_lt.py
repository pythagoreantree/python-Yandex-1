ilist = input().split()
input_list = [int(j) for j in ilist]
current_elem = input_list[0]
vozrastaet = True
for i in range(1, len(input_list)):
    if input_list[i] > current_elem:
        current_elem = input_list[i]
    else:
        vozrastaet = False
if vozrastaet:
    print('YES')
else:
    print('NO')
