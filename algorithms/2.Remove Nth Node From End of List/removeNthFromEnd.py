# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        res = ListNode(0)
        if not head:
            return None
        res.next = head
        length = 0
        first = head
        
        while first:
            length += 1
            first = first.next
        
        length -= n
        first = res
        while length > 0:
            length -= 1
            first = first.next

        # the collected list node will be head[length - n - 1:]
        first.next = first.next.next # head is also updated 
        return res.next

# Refered other resolution
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        first = second = head
        for _ in range(n):
            first = first.next
        
        if not first:
            return head.next
        
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head
            
