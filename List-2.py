def count_evens(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i]%2==0:
            count+=1
    return count

def big_diff(nums):
    return max(nums)-min(nums)

def centered_average(nums):
    x = min(nums)
    y = max(nums)
    skippedX = 0
    skippedY = 0
    temp = []
    for i in range(len(nums)):
        if (nums[i]!=x or skippedX<=1) and (nums[i]!=y or skippedY<=1):
            temp.append(nums[i])
        elif nums[i]==x:
            skippedX+=1
        elif nums[i]==y:
            skippedY+=1
    sumVal = 0
    for n in range(len(temp)):
        sumVal += temp[n]
    if len(temp)>0:
        return int(sumVal/len(temp))
    else:
        return 0

print(centered_average([1,1,100]))