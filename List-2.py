def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]%2==0:
            count+=1
    return count

print(count_evens([1,2,3,5,2]))