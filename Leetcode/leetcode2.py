import copy

nums = [3,3]
target = 6

def twoSum(nums,target):
    nums1 = copy.deepcopy(nums)
    for num1 in nums:
        for num2 in nums1:
            if num1+num2 == target and nums.index(num1) != nums.index(num2):
                return [nums.index(num1),nums.index(num2)]

result = twoSum(nums, target)

print(result)