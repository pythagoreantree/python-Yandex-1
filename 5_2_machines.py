n, k = map(int, input().split())
nums = list(map(int, input().split()))

first_pointer = 0
second_pointer = 0

counter = 0

summa = 0
while second_pointer < n:
    if summa < k:
        summa += nums[second_pointer]
        if summa < k:
            second_pointer += 1
    elif summa >= k:
        if summa == k:
            counter += 1
        summa -= nums[first_pointer]
        first_pointer += 1
        if summa < k:
            second_pointer += 1
print(counter)
