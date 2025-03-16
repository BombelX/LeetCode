# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        curr = head
        ll_len = 0
        while curr is not None:
            ll_len += 1
            curr = curr.next
        
        node_to_del = ll_len-(n-1)
        if node_to_del == 1:
            return head.next
        else:
            index = 1
            curr = start
            prev = None
            while curr is not None:
                if index == node_to_del-1:
                    if curr.next is not None:
                        curr.next = curr.next.next
                    else:
                        curr.next = None
                    return start
                
                index+=1
                curr = curr.next
        