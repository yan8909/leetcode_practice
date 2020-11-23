# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:
# Input: [3,2,3]
# Output: 3

# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums) -> int:
        dic = dict()
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        max_val = 0
        max_key = 0
        for key, val in dic.items():
            if val > max_val:
                max_val = val
                max_key = key
        return max_key


