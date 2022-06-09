#Three Number Sum
#no repeating data, give pos and neg numbers, go through this lists
#find triplets that equal given number

nums = [2,7,11,15]
target = 9

def twoSum (nums):
    for i in nums:
        for j in nums:
            if i + j == target:
                return [nums.index(i), nums.index(j)]

print(twoSum(nums))