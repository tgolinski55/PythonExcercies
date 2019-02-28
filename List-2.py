def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]%2==0:
            count+=1
    return count

def big_diff(nums):
    return max(nums)-min(nums)

print(big_diff([1,2,3,5,2]))