# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

# Find all the elements of [1, n] inclusive that do not appear in this array.

# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# Example:

# Input:
# [4,3,2,7,8,2,3,1]

# Output:
# [5,6]


class Solution:
    def findDisappearedNumbers(self, nums):
        # 例原本完整array應為[1,2,3,4,5,6,7,8]
        # 以input[4,3,2,7,8,2,3,1]為例
        # 第一個數4，原本的位置應為array[3]
        # 因此將input[3]的值變為負，作為標記
        # 最後為正的值的位置便為答案
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -nums[index] if nums[index] > 0 else nums[index]

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0 :
                ans.append(i+1)
        return ans