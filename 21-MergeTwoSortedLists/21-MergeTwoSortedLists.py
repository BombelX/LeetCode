# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val < list2.val:
                prim = list1
                sec = list2
            else:
                prim = list2
                sec = list1
            prev = None
            start = prim
            while prim is not None and sec is not None:
                if prim.val <= sec.val:
                    prev = prim
                    prim = prim.next

                else:
                    tmp = sec.next
                    sec.next = prim
                    prev.next = sec
                    prev = sec
                    sec = tmp

                                        
            if prim == None and sec == None:
                return start
            elif prim == None:
                prev.next = sec
                return start
            else:
                return start