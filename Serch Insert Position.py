# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the 
# index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Input: nums = [1,3,5,6], target = 7
# Output: 4

nums = [1,3,5,6]
target = 5

def SerchInsertPosition(nums, target):
    find=False
    for i in range (0, len(nums)):
        if(nums[i]==target):
            return i
            find = True
    i=0
    while (find == False):
        if (i == len(nums)):
            return i
            find = True
        elif(nums[i]<target):
            i = i+ 1
        else: 
            return i
            find = True

print(SerchInsertPosition(nums, target))