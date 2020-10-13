# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example :
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = out = ListNode(0)
        carry = 0
        res = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # 取list1值
            v2 = l2.val if l2 else 0 # 取list2值
            sum = v1 + v2 + carry
            res = sum % 10 # 取餘數
            carry = sum // 10 # 計算進位，取商
            out.next = ListNode(res)
            out = out.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ans.next

"""
l1=[5,4,5]
l2=[5,6,4]

carry=0
------
l1=[5,4,5]
l2=[5,6,4]
v1=5
v2=5
sum=10
res=0
carry=1

head
 0-> 0
--------
l1=[4,5]
l2=[6,4]
v1=4
v2=6
sum=11
res=1
carry=1

head
 0-> 0 -> 1
-------
l1=[5]
l2=[4]
v1=5
v2=4
sum=10
res=0
carry=1

head
 0-> 0 -> 1 -> 0
------
l1=None
l2=None
v1=0
v2=0
sum=1
res=1
carry=0

head
 0-> 0 -> 1 -> 0 -> 1
 """
