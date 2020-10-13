# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example :

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].


class Solution:
    # approach 1 迴圈依序尋找答案
    def twoSum_v1(self, nums, target: int):
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
    
    # approach 2 字典
    def twoSum_v2(self, nums, target: int):
        dic = {}
        for i in range (len(nums)):
            co = target - nums[i]
            if co in dic:
                return [dic[co], i]
            else:
                dic[nums[i]] = i



test = Solution()
array = [2,7,11,15]
print(test.twoSum_v2(array, 17))