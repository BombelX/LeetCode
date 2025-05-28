# Last updated: 28.05.2025, 19:20:48
# Definition for singly-linked list.
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        start = head.next
        curr = Node("start",head)
        prev = curr
        curr = curr.next
        while curr is not None and curr.next is not None:
                tmp1,tmp2,tmp3 = curr,curr.next,curr.next.next
                prev.next = tmp2
                tmp2.next  = tmp1
                tmp1.next = tmp3
                prev = tmp1
                curr = tmp3
        return start


            