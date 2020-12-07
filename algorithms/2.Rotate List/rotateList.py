# 61. Rotate List
# https://leetcode.com/problems/rotate-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # already checked solution
        if not head:
            return None
        
        lastElement = head
        length = 1
        while lastEle.next: # get the length of list
            lastElement = lastElement.next
            length += 1
        
        # k = 0 if k is equal to the length of the list
        # else k = k % length (if k is greater than the length of the list)
        k = k % length 
        lastElement.next = head # set the last node to point to head node
        tmpNode = head
        for _ in range(length - k - 1):
            tmpNode = tmpNode.next
        
        res = tmpNode.next
        tmpNode.next = None

        return res