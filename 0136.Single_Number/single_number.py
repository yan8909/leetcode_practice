# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        if i not in nums:
            res.append(i)
        else:
            res.remove(i)
        return res[i] 

# Solution 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # (1+2+3)*2 - (1+1+2+2+3) = 3
        return sum(set(nums))*2 - sum(nums) 
        