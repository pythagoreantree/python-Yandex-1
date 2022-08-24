nums = [int(i) for i in input().split()]

counter = 0
for j in range(1, len(nums)-1):
    if nums[j] > nums[j-1] and nums[j] > nums[j+1]:
        counter += 1
print(counter)
