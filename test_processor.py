ans1 = []
with open('1_7_B_003_test', 'r') as file_obj:
    for line in file_obj.readlines():
        ans1 = list(map(int, line.split()))

ans2 = []
with open('myOutFile.txt', 'r') as file_obj:
    for line in file_obj.readlines():
        ans2 = list(map(int, line.split()))

for i in range(len(ans1)):
    if ans1[i] != ans2[i]:
        print(i, ans1[i], ans2[i])

