# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[end] = nums[i]
                end += 1
                
        # fill remaining array with 0's
        for i in range(end, len(nums)):
            nums[i] = 0